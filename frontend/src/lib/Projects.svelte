<script>
  import { GithubIcon, CloudIcon } from 'svelte-feather-icons';
  import { onMount } from 'svelte';

  let projects = [];

  onMount(async () => {
    fetch('http://127.0.0.1:8000/project/')
      .then((response) => response.json())
      .then((data) => {
        projects = data;
      })
      .catch(() => {
        return [];
      });
  });
</script>

<section class="hero is-fullheight projects-section">
  <div class="section-pattern" aria-hidden="true"></div>
  <div class="container is-fluid">
    <div class="columns is-multiline mx-2 my-6">
      {#each projects as project}
        <div class="column is-full">
          <div class="container-project m-auto">
            <div class="container-img">
              <img class="" src={project.pro_img} alt={project.name || 'Project preview'} />
            </div>
            <div class="container-info">
              <h4 class="custom-title">{project.name}</h4>
              <p class="paragraph custom-text">{project.description}</p>

              <div class="custom-container-tecno">
                {#each project.technologys as technology}
                  <i class={technology.icon}></i>
                {/each}
              </div>
              <div class="container-code">
                <a href={project.link_repo} target="”_blank”">
                  <button class="button cta-primary custom-buttom-color is-normal is-rounded">
                    <span class="icon">
                      <GithubIcon size="24" />
                    </span>
                    <span>GitHub</span>
                  </button>
                </a>
                <a href={project.link_live} target="”_blank”">
                  <button class="button cta-primary custom-buttom-color is-normal is-rounded">
                    <span class="icon">
                      <CloudIcon size="24" />
                    </span>
                    <span>Live</span>
                  </button>
                </a>
              </div>
            </div>
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>

<style>
  .container-project {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
  }

  .container-img {
    margin: 8px;
    width: 600px;
  }

  .container-info {
    margin: 8px;
    text-align: center;
    width: 682px;
  }

  .container-code {
    margin: 12px;
  }

  .custom-container-tecno i {
    font-size: 16px;
    margin: 4px;
  }

  .paragraph {
    text-align: center;
    padding: 16px;
    font-family: 'Inconsolata', monospace;
    line-height: 1.25rem;
    color: var(--color-text);
  }

  .custom-title {
    font-size: 36px;
    font-family: 'Inconsolata', monospace;
    color: var(--color-text);
  }

  .custom-buttom-color {
    background-color: var(--color-accent);
    width: 105px;
    color: var(--color-on-accent);
    border: none;
  }

  .custom-container-tecno {
    display: flex;
    flex-direction: row;
    justify-content: center;
    height: 30px;
    margin: 16px;
    color: gray;
  }

  :global(body.dark-mode) .custom-container-tecno {
    display: flex;
    flex-direction: row;
    justify-content: center;
    height: 30px;
    margin: 16px;
    color: white;
  }

  .projects-section {
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

  .container-project {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
  }

  .container-img {
    margin: 8px;
    width: 600px;
  }

  .container-info {
    margin: 8px;
    text-align: center;
    width: 682px;
  }

  .container-code {
    margin: 12px;
  }

  .custom-container-tecno i {
    font-size: 16px;
    margin: 4px;
    color: var(--color-muted);
  }

  .paragraph {
    text-align: center;
    padding: 16px;
    font-family: 'Inconsolata', monospace;
    line-height: 1.25rem;
    color: var(--color-text);
  }

  .custom-title {
    font-size: 36px;
    font-family: 'Inconsolata', monospace;
    color: var(--color-text);
  }

  .custom-buttom-color {
    background-color: var(--color-accent);
    width: 105px;
    color: var(--color-on-accent);
    border: none;
  }

  /* Modo oscuro */

  img {
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
</style>
