<script>
  import { FileTextIcon,DownloadIcon } from 'svelte-feather-icons'

  import Animate from './Animate.svelte';
  import { onMount } from "svelte";



  let abouts = [];

onMount(async () => {
  fetch("http://127.0.0.1:8000/about/")
    .then((response) => response.json())
    .then((data) => {
      abouts = data;
      console.log(abouts);
      // console.log(data);
    })
    .catch((error) => {
      // console.log(error);
      return [];
    });
});


let downloadCV = async () => {
        try {
            let response = await fetch('http://vic.uy/download_cv/');
            response.blob().then(blob => {
                let url = window.URL.createObjectURL(blob);
                let a = document.createElement('a');
                a.style.display = 'none';
                a.href = url;
                a.download = 'cv.pdf';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
            });
        } catch (error) {
            // console.error(error);
        }
    };
</script>



<Animate>
<section class="hero is-fullheight custom-component"  >
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
          <a href=""  on:click={downloadCV}>
            <button class="button custom-bottom   is-normal is-rounded">
              <span class="icon">
                <DownloadIcon size="24" />
              </span>
              <span>CV</span>
            </button>
          </a>
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

    <div class="column is-half ">
      <div class="container" >
        <h3 class="title title__bio custom-text">Bio</h3>
        <div>
          <p class="paragraph custom-text"></p>
        </div>
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
    text-align: justify;
  }

  

 
  .custom-component {
        background-color: #fffffe;
    }


    


:global(body.dark-mode) .custom-component {
        background-color: #0f0e17;
        color: #fffffe;
    }


.custom-text {
        color: #1f1235;
}

:global(body.dark-mode) .custom-text {
        color: #f0f0f0;
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


</style>
