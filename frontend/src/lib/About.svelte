<script>
  import { DownloadIcon } from 'svelte-feather-icons';
  import Carrusel from './Carrusel.svelte';
  import Animate from './Animate.svelte';
  import { onMount } from 'svelte';
  import fileSaver from 'file-saver';
  const { saveAs } = fileSaver;

  let abouts = [];
  let certificates = [];

  onMount(async () => {
    try{
      const[aboutResponse,certificateResponse] = await Promise.all([
        fetch("https://vic.uy/about/").then((response) => response.json()),
        fetch("https://vic.uy/certificates/").then((response) => response.json())
      ]);
      abouts = aboutResponse;
      certificates = Object.values(certificateResponse);
    } catch {
      // ignore
    }
  });

  async function downloadCV() {
    try {
      // Realiza una solicitud al servidor para obtener el archivo PDF
      let response = await fetch('https://vic.uy/download_cv/');
      let blob = await response.blob();
      saveAs(blob, 'cv.pdf');
    } catch (error) {
      console.error(error);
    }
  }
</script>

<Animate>
  <section class="hero is-fullheight about-section">
    <div class="section-pattern" aria-hidden="true"></div>
    {#each abouts as about}
      <div class="columns is-multiline mx-2 my-6">
        <div class="column"></div>
        <div class="column is-one-third">
          <div class="container about-img">
            <img src={about.imagenabout} alt="" />
          </div>
        </div>
        <div class="column is-one-third-desktop">
          <div class="container about-info">
            <h3 class="title custom-text">{about.title}</h3>
            <p class="paragraph custom-text">{about.description}</p>
            <div class="btn-cv">
              <button
                class="button cta-primary custom-bottom is-normal is-rounded"
                on:click={downloadCV}
              >
                <span class="icon">
                  <DownloadIcon size="24" />
                </span>
                <span>CV</span>
              </button>
            </div>
          </div>
        </div>
        <div class="column"></div>
      </div>
      <div class="columns is-multiline">
        <div class="column"></div>
        <div class="column is-half m-auto">
          <div class="container">
            <h4 class="title custom-text">Skills and Tools</h4>
            <p class="subtitle custom-text">Skills and technologies that I use in my projects.</p>
          </div>
          <div class="container-tools">
            <div class="box-tools">
              <i class="devicon-django-plain custom-icon custom-box-tools"></i>
              <p class="custom-text">Django</p>
            </div>
            <div class="box-tools">
              <i class="devicon-html5-plain custom-icon custom-box-tools"></i>
              <p class="custom-text">HTML5</p>
            </div>
            <div class="box-tools">
              <i class="devicon-css3-plain custom-icon custom-box-tools"></i>
              <p class="custom-text">CSS3</p>
            </div>
            <div class="box-tools">
              <i class="devicon-python-plain custom-icon custom-box-tools"></i>
              <p class="custom-text">Python</p>
            </div>
            <div class="box-tools">
              <i class="devicon-linux-plain custom-icon custom-box-tools"></i>
              <p class="custom-text">Linux</p>
            </div>
            <div class="box-tools">
              <i class="devicon-bootstrap-plain custom-icon custom-box-tools"></i>
              <p class="custom-text">Bootstrap</p>
            </div>
            <div class="box-tools">
              <i class="devicon-docker-plain custom-icon custom-box-tools"></i>
              <p class="custom-text">Docker</p>
            </div>
            <div class="box-tools">
              <i class="devicon-svelte-plain custom-icon custom-box-tools"></i>
              <p class="custom-text">Svelte</p>
            </div>
          </div>
        </div>
        <div class="column"></div>
      </div>

      <div class="columns p-6">
        <div class="column"></div>

        <div class="column is-one-third-desktop">
          <div class="container">
            <h3 class="title title__bio custom-text">Certificates</h3>
            <Carrusel {certificates}></Carrusel>
          </div>
        </div>
        <div class="column"></div>
      </div>
    {/each}
  </section>
</Animate>

<style>
  .title {
    font-family: 'Karla', sans-serif;
    text-align: center;
    color: var(--color-text);
  }

  .subtitle {
    text-align: center;
    color: var(--color-muted);
  }

  .about-info {
    width: 100%;
    text-align: center;
  }

  .about-img img {
    height: 100%;
    width: 100%;
    object-fit: contain;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .container-tools {
    display: flex;
    flex-direction: row;
    justify-content: center;
    flex-wrap: wrap;
    width: auto;
    height: auto;
    margin: 36px;
  }

  .box-tools {
    margin: 10px;
    height: 90px;
    width: auto;
  }
  .box-tools i {
    font-size: 70px;
  }
  .box-tools p {
    text-align: center;
    margin: 3px;
  }

  .btn-cv {
    height: auto;
    width: auto;
    margin: 36px;
  }

  .paragraph {
    text-align: justify;
    padding: 16px;
    font-family: 'Inconsolata', monospace;
    line-height: 1.7rem;
    color: var(--color-text);
    margin: 20px 0;
  }

  .title__bio {
    font-family: 'Karla', sans-serif;
    color: #fffffe;
    text-align: center;
  }

  .custom-icon {
    color: var(--color-muted);
  }

  .custom-bottom {
    background-color: var(--color-accent);
    width: 105px;
    color: var(--color-on-accent);
  }

  .custom-box-tools {
    color: var(--color-accent);
  }

  .about-section {
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
  .title__bio {
    font-family: 'Karla', sans-serif;
    text-align: center;
    color: var(--color-text);
  }

  .subtitle {
    text-align: center;
    color: var(--color-muted);
  }

  .paragraph {
    text-align: justify;
    padding: 16px;
    font-family: 'Inconsolata', monospace;
    line-height: 1.7rem;
    color: var(--color-text);
    margin: 20px 0;
  }

  .custom-icon,
  .box-tools p {
    color: var(--color-muted);
  }

  .custom-bottom {
    background-color: var(--color-accent);
    color: var(--color-on-accent);
    width: 105px;
  }

  /* Modo oscuro */
</style>
