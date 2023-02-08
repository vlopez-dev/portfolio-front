<script>
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

</script>
<Animate>
<section class="hero is-fullheight" style="outline: 2px solid white;" >
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

          <h3 class="title">{about.title}</h3>
          <p class="paragraph">{about.description}</p>
          <div class="btn-cv">
          <a href="">
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
        <h4 class="title">Skills and Tools</h4>
        <p class="subtitle">Skills and technologies that I use in my projects.</p>
      </div>
      <div class="container-tools">
          <div class="box-tools">


            <i class="devicon-django-plain"></i>
                      <p>Django</p>
          
        </div>
        <div class="box-tools">
          <i class="devicon-html5-plain"></i>
          <p>HTML5</p>
        </div>
        <div class="box-tools">

          <i class="devicon-css3-plain"></i>
          <p>CSS3</p>
        </div>
        <div class="box-tools">
          <i class="devicon-python-plain"></i>
          <p>Python</p>
        </div>
        <div class="box-tools">
          <i class="devicon-linux-plain"></i>
          <p>Linux</p>
        </div>
        <div class="box-tools">

          <i class="devicon-bootstrap-plain"></i>
          <p>Bootstrap</p>
          
        </div>
        <div class="box-tools">

          <i class="devicon-docker-plain"></i>
          
          <p>Docker</p>
          
        </div>
        <div class="box-tools">


          <i class="devicon-svelte-plain"></i>
                    
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
        <h3 class="title title__bio">Bio</h3>
        <div>
          <p class="paragraph">{about.bio}</p>
        </div>
      </div>

    </div>
    <div class="column"></div>

  </div>


  <div class="columns p-6">
    <div class="column"></div>
    <div class="column is-half p-6 ">
      <div class="container">

      <h3 class="title title__bio">Career</h3>
        <h6>Support Enginer<span>-</span>02/2007 - Actualidad</h6>
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
  section {
    background-color: #0f0e17;
  }

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

  

</style>
