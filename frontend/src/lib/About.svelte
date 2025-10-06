<script>
  
  import { FileTextIcon,DownloadIcon } from 'svelte-feather-icons'
  import Carrusel from './Carrusel.svelte';
  import Animate from './Animate.svelte';
  import { onMount } from "svelte";
  import fileSaver from 'file-saver';
   const { saveAs } = fileSaver;
  


let abouts = [];
let certificates = [];


  onMount(async () => {
    try{
      const[aboutResponse,certificateResponse] = await Promise.all([
        fetch("http://127.0.0.1:8000/about/").then((response) => response.json()),
        fetch("http://127.0.0.1:8000/certificates/").then((response) => response.json())
      ]);
      abouts = aboutResponse;
      certificates = Object.values(certificateResponse);

    }catch(error){
      console.log(error);
    }
  });





    async function downloadCV() {
    try {
      // Realiza una solicitud al servidor para obtener el archivo PDF
      let response = await fetch('http://127.0.0.1:8000/download_cv/');
      let blob = await response.blob();
      // Utiliza saveAs para iniciar la descarga del archivo en el navegador
      saveAs(blob, 'cv.pdf');
    } catch (error) {
      console.error(error);
    }
  }
</script>



<Animate>
<section class="hero is-fullheight about-section"  >
  {#each abouts as about}
    <div class="columns is-multiline mx-2 my-6" >
        <div class="column "></div>
        <div class="column is-one-third">
          <div class="container about-img">
            <img src="{about.imagenabout}" alt="">
          </div>
        </div>
        <div class="column is-one-third-desktop">
          <div class="container about-info">

          <h3 class="title custom-text">{about.title}</h3>
          <p class="paragraph custom-text">{about.description}</p>
          <div class="btn-cv">
            <button class="button custom-bottom   is-normal is-rounded" on:click={downloadCV}>
              <span class="icon">
                <DownloadIcon size="24" />
              </span>
              <span>CV</span>
            </button>
          </div>
        </div>
        </div>
        <div class="column">
        </div>
    </div>
  <div class="columns is-multiline">
    <div class="column ">
    </div>
    <div class="column is-half m-auto">
      <div class="container">
        <h4 class="title custom-text">Skills and Tools</h4>
        <p class="subtitle custom-text">Skills and technologies that I use in my projects.</p>
      </div>
      <div class="container-tools">
          <div class="box-tools ">
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
          <i class="devicon-python-plain custom-icon custom-box-tools "></i>
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
    <div class="column">
    </div>
  </div>

  <div class="columns p-6">
    <div class="column"></div>

    <div class="column is-one-third-desktop ">
      <div class="container" >
        <h3 class="title title__bio custom-text">Certificates</h3>
       <Carrusel certificates={certificates}></Carrusel>
      </div>

    </div>
    <div class="column"></div>

  </div>

  {/each}

</section>

</Animate>


<style>


  .title {
    font-family: "Karla", sans-serif;
    text-align: center;
    color: #fffffe;
  }

  .subtitle{
    text-align: center;
    color: #a7a9be;
  }


  .about-info{
    width: 100%;
    text-align: center;
  }

  .about-img{
    height: 80%;
  }
  .about-img img{
    height: 100%;
    width: 100%;
    object-fit: contain;
    
  }


  

  .container-tools{
    display: flex;
    flex-direction: row;
    justify-content: center;
    flex-wrap: wrap;
    width: auto;
    height: auto;
    margin: 36px;
    }

  
  .box-tools{
    margin: 10px;
    height: 90px;
    width: auto;
    
  }
  .box-tools i{
    font-size: 70px;
  }
  .box-tools p{
    text-align: center;
    margin: 3px;
  }

  .btn-cv{
    height: auto;
    width: auto;
    margin: 36px;
  }


  .paragraph{
    text-align: justify;
    padding: 16px;
    font-family: "Inconsolata", monospace;
    line-height: 1.70rem;
    color: #a7a9be;
    margin: 20px 0;
  }


  .title__bio{
    font-family: "Karla", sans-serif;
    color: #fffffe;
    text-align: center;
  }

  

 

    




.custom-icon{
  color: #a7a9be;
}

:global(body.dark-mode) .custom-icon {
        color: #f0f0f0;
}



.custom-bottom{
  background-color: #ff6e6c;
  width: 105px;
  color: #fffffe;
}


:global(body.dark-mode) .custom-bottom {
  background-color: #ff8906;
    border: none;
    color: #fffffe;
    width: 105px;
    box-shadow: -8px 0px 20px rgba(255, 146, 26, 0.3), 0px 0px 20px rgba(255, 146, 26, 0.3), 8px 0px 20px rgb(255 146 26 / 30%);

}









.custom-box-tools{
  color: #ff6e6c;
}

:global(body.dark-mode) .custom-icon {
        color: #f0f0f0;
}

.about-section {
  background-color: #EDE7F6;
  color: #3E3A4D;
  transition: background-color 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.title,
.title__bio {
  font-family: "Karla", sans-serif;
  text-align: center;
  color: #3E3A4D;
}

.subtitle {
  text-align: center;
  color: #6A5C93; /* tono intermedio lavanda */
}

.paragraph {
  text-align: justify;
  padding: 16px;
  font-family: "Inconsolata", monospace;
  line-height: 1.70rem;
  color: #5C5470;
  margin: 20px 0;
}

.custom-icon,
.box-tools p {
  color: #6A5C93;
}

.custom-bottom {
  background-color: #B39DDB;
  color: #3E3A4D;
  width: 105px;
}

/* Modo oscuro */
:global(body.dark-mode) .about-section {
  background-color: #3E3A4D;
  color: #EDE7F6;
}

:global(body.dark-mode) .title,
:global(body.dark-mode) .title__bio,
:global(body.dark-mode) .paragraph,
:global(body.dark-mode) .subtitle {
  color: #EDE7F6;
}

:global(body.dark-mode) .custom-icon {
  color: #EDE7F6;
}

:global(body.dark-mode) .custom-bottom {
  background-color: #9575CD;
  color: #EDE7F6;
  box-shadow: 0 0 10px rgba(179, 157, 219, 0.4);
}



</style>
