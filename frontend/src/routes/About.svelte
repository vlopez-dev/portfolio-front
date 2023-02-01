<script>
  export let about_title, about_description, src;
  import Animate from './Animate.svelte';

</script>
<Animate>
<section class="hero is-fullheight"  >
    <div class="columns is-multiline m-6" >
        <div class="column "></div>
        <div class="column is-one-third">
          <div class="container about-img">
            <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80" alt="">
          </div>
        </div>
        <div class="column">
          <div class="container about-info">
          <h3 class="title">Titulo</h3>
          <p class="paragraph">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus temporibus nisi molestias repellendus iste nihil deserunt distinctio ab! Aliquam doloremque laudantium aut dignissimos reiciendis maxime sed ea, a repudiandae corrupti.</p>
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
    <div class="column"></div>
  </div>


  
  
</section>

<section class="hero is-fullheight">
  <div class="columns is-half m-auto">
    <div class="column"></div>

    <div class="column is-half">
      <div class="container">
        <h3 class="title">Titulo</h3>
        <p class="paragraph">Lorem ipsum dolor sit amet consectetur adipisicing elit. Animi asperiores, aliquid voluptas unde veritatis, quasi in minima modi ea inventore accusantium distinctio perspiciatis voluptatem excepturi numquam ut ducimus hic suscipit.</p>
      </div>
    </div>
    <div class="column"></div>
  </div>
  
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
    text-align: center;
    padding: 16px;
    font-family: "Inconsolata", monospace;
    line-height: 1.25rem;
    color: #a7a9be;
  }
</style>
