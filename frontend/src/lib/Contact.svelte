<script>
  import { SendIcon } from 'svelte-feather-icons';

  import Animate from './Animate.svelte';
  import { onMount } from 'svelte';

  let message;
  let email;
  let contacts = [];

  onMount(async () => {
    fetch('http://127.0.0.1:8000/contact/')
      .then((response) => response.json())
      .then((data) => {
        contacts = data;
      })
      .catch(() => {
        return [];
      });
  });

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + '=') {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  const sendEmail = async () => {
    const csrfCookie = getCookie('csrftoken');

    const recaptchaResponse =
      typeof window !== 'undefined' && window.grecaptcha ? window.grecaptcha.getResponse() : null;

    const response = await fetch('http://127.0.0.1:8000/send_email/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfCookie,
      },
      body: JSON.stringify({ message, email, recaptchaResponse }),
      credentials: 'include',
    });

    if (!response.ok) {
      document.getElementById('status').textContent =
        'Error al enviar el mensaje, inténtalo nuevamente';
    } else {
      document.getElementById('status').textContent = 'Mensaje enviado con éxito';
    }
  };
</script>

<Animate>
  <section class="hero is-fullheight contact-section">
    <div class="section-pattern" aria-hidden="true"></div>
    <div class="columns is-multiline mx-2 my-6">
      <div class="column"></div>
      <div class="column is-one-third">
        <div class="container">
          {#each contacts as contact}
            <h4 class="title custom-title">{contact.title}</h4>
            <p class="custom-text">{contact.description}</p>
          {/each}
          <div class="custom-message" id="status" role="status" aria-live="polite"></div>
        </div>
        <form class="mt-6" action="" on:submit|preventDefault={sendEmail}>
          <div class="field">
            <label class="label custom-label" for="email">Email</label>
            <div class="control has-icons-left has-icons-right">
              <input
                id="email"
                class="input custom-input"
                type="email"
                bind:value={email}
                placeholder="Email input"
                required
                aria-required="true"
              />
              <span class="icon is-small is-left">
                <i class="fas fa-envelope"></i>
              </span>
              <span class="icon is-small is-right">
                <i class="fas fa-exclamation-triangle"></i>
              </span>
            </div>
          </div>

          <div class="field">
            <label class="label custom-label" for="messageInput">Message</label>
            <div class="control">
              <textarea
                id="messageInput"
                class="textarea custom-input"
                bind:value={message}
                placeholder="Message"
                rows="4"
                required
                aria-required="true"
              ></textarea>
            </div>
          </div>

          <div class="field is-grouped is-justify-content-center">
            <div class="control btn-cv">
              <button class="button cta-primary custom-button is-normal is-rounded">
                <span>
                  <SendIcon size="24" />
                </span>
                Send</button
              >
            </div>
          </div>
        </form>
        <div class="column">
          <div class="container">
            <div class="g-recaptcha" data-sitekey="6Ld7NskkAAAAAJKzdpVtsTXKBUdX_TT3dizQHxA8"></div>
          </div>
        </div>
      </div>

      <div class="column"></div>
    </div>
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>
  </section>
</Animate>

<style>
  .title {
    font-family: 'Karla', sans-serif;
    text-align: center;
    color: var(--color-text);
  }

  .custom-title {
    color: var(--color-text);
    text-align: center;
  }

  .custom-button {
    background-color: var(--color-accent);
    border: none;
    color: var(--color-on-accent);
    width: 105px;
    margin-bottom: 15px;
  }

  .custom-input {
    border-color: var(--color-border);
    background-color: var(--color-surface);
    color: var(--color-text);
  }

  :global(body.dark-mode) .custom-input {
  }

  .custom-label {
    color: var(--color-text);
  }

  .custom-text {
    text-align: justify;
    color: var(--color-text);
    font-family: 'Inconsolata', monospace;
    line-height: 1.7rem;
  }

  .custom-message {
    color: var(--color-success);
    text-align: center;
  }

  .g-recaptcha {
    margin: 0 auto;
    width: 304px;
  }

  .contact-section {
    background-color: var(--color-bg);
    color: var(--color-text);
    position: relative;
    overflow: hidden;
    transition: background-color 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .section-pattern {
    position: absolute;
    inset: 0;
    height: 140px;
    pointer-events: none;
    opacity: 0.03;
    background-image: radial-gradient(circle at 1px 1px, var(--color-text) 1px, transparent 1.5px);
    background-size: 18px 18px;
    mix-blend-mode: multiply;
  }

  .title,
  .custom-title {
    font-family: 'Karla', sans-serif;
    text-align: center;
    color: var(--color-text);
  }

  .custom-text {
    text-align: justify;
    color: var(--color-text);
    font-family: 'Inconsolata', monospace;
    line-height: 1.7rem;
  }

  .custom-label {
    color: var(--color-text);
  }

  .custom-input {
    border-color: var(--color-border);
    background-color: var(--color-surface);
    color: var(--color-text);
  }

  .custom-button {
    background-color: var(--color-accent);
    border: none;
    color: var(--color-on-accent);
    width: 105px;
    margin-bottom: 15px;
  }

  .custom-message {
    color: green;
    text-align: center;
  }

  /* Modo oscuro */
</style>
