<script>
  import { GithubIcon } from 'svelte-feather-icons'

  export let about_title, about_description, src;
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
      console.log(error);
      return [];
    });
});


let downloadCV = async () => {
        try {
            let response = await fetch('http://127.0.0.1:8000/download_cv/');
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
            console.error(error);
        }
    };



</script>



<Animate>
    <!-- aqui tu contenido -->
<section class="hero is-fullheight custom-component"  >
  {#each abouts as about}

    <div class="columns is-multiline m-6" >
        <div class="column "></div>
        <div class="column is-one-third">
          <div class="container about-img">
            <img src="{about.imagenabout}" alt="">
          </div>
        </div>
        <div class="column">
          <div class="container about-info">

          <h3 class="title custom-text">{about.title}</h3>
          <p class="paragraph custom-text">{about.description}</p>
          <div class="btn-cv">
          <a href=""  on:click={downloadCV}>
            <button class="button">
  
              <span class="icon">
                <img src="https://img.icons8.com/ios/50/ffffff/parse-resumes.png"/>
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
          <div class="box-tools">


            <i class="devicon-django-plain custom-icon"></i>
                      <p>Django</p>
          
        </div>
        <div class="box-tools">
          <i class="devicon-html5-plain custom-icon"></i>
          <p>HTML5</p>
        </div>
        <div class="box-tools">

          <i class="devicon-css3-plain custom-icon"></i>
          <p>CSS3</p>
        </div>
        <div class="box-tools">
          <i class="devicon-python-plain custom-icon "></i>
          <p>Python</p>
        </div>
        <div class="box-tools">
          <i class="devicon-linux-plain custom-icon"></i>
          <p>Linux</p>
        </div>
        <div class="box-tools">

          <i class="devicon-bootstrap-plain custom-icon"></i>
          <p>Bootstrap</p>
          
        </div>
        <div class="box-tools">

          <i class="devicon-docker-plain custom-icon"></i>
          
          <p>Docker</p>
          
        </div>
        <div class="box-tools">


          <i class="devicon-svelte-plain custom-icon"></i>
                    
          <p>Svelte</p>
          
        </div>
      </div>
      
    </div>
    <div class="column">
    </div>
  </div>

  <div class="columns p-6">
    <div class="column"></div>

    <div class="column is-half p-6 ">
      <div class="container" >
        <h3 class="title title__bio custom-text">Bio</h3>
        <div>
          <p class="paragraph custom-text">{about.bio}</p>
        </div>
      </div>

    </div>
    <div class="column"></div>

  </div>


  <div class="columns p-6">
    <div class="column"></div>
    <div class="column is-half p-6 ">
      <div class="container">

      <h3 class="title title__bio custom-text">Career</h3>
        <h6 class="custom-text">Support Enginer<span>-</span>02/2007 - Actualidad</h6>
        <a href="">AMEC</a>
        <p>lorem</p>
      </div>
    </div>
    <div class="column m-auto"></div>
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

  .btn-cv button{
    background-color: #ff8906;
    border: none;
    color: #fffffe;
    width: 90px;
    box-shadow: -8px 0px 20px rgba(255, 146, 26, 0.3), 0px 0px 20px rgba(255, 146, 26, 0.3), 8px 0px 20px rgb(255 146 26 / 30%);

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

.custom-subtitle{
  color: #1b1425;
}


.custom-icon{
  color: #a7a9be;
}

:global(body.dark-mode) .custom-icon {
        color: #f0f0f0;
}

</style>
