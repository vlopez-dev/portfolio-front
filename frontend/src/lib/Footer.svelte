<script>
  import { GithubIcon, LinkedinIcon, TwitterIcon } from 'svelte-feather-icons';
</script>

<footer class="footer m-auto custom-component">
  <div class="content has-text-centered">
    <p></p>
    <div class="social">
      <div class="box_social custom-icons">
        <a href="https://twitter.com/vic_mde" class="custom-icons" target="_blank">
          <TwitterIcon size="24" />
        </a>
      </div>
      <div class="box_social custom-icons">
        <a href="https://github.com/vlopez-dev" class="custom-icons" target="_blank">
          <GithubIcon size="24" />
        </a>
      </div>
      <div class="box_social custom-icons">
        <a href="https://www.linkedin.com/in/victorlopezr/" class="custom-icons" target="_blank">
          <LinkedinIcon size="24" />
        </a>
      </div>
    </div>
  </div>
</footer>

<style>
  .footer {
    height: 80px;
    width: 100%;
    background-color: var(--color-bg);
    box-shadow: none;
    border-top: none;
    backdrop-filter: none;
    position: relative;
    margin-top: 0;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }

  a,
  p {
    color: var(--color-text);
    font-family: 'Karla', sans-serif;
    padding: 10px;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .social {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: auto;
    width: auto;
  }

  .social a {
    padding: 8px;
    border-radius: 50%;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .social a:hover {
    background-color: var(--color-accent);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 182, 185, 0.2);
  }

  .box_social {
    margin: 8px;
  }

  .custom-icons {
    color: var(--color-text);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .custom-icons:hover {
    color: white;
    transform: scale(1.1);
  }
</style>
