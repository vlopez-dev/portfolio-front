<script>
  export let about_title, about_description, src;
</script>

<section class="hero is-fullheight">
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
          <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus temporibus nisi molestias repellendus iste nihil deserunt distinctio ab! Aliquam doloremque laudantium aut dignissimos reiciendis maxime sed ea, a repudiandae corrupti.</p>
          <a href="">
            <button class="button">
  
              <span class="icon">
                <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png"/>
              </span>
              <span>CV</span>
  
            </button>
          </a>
        </div>
        </div>
        <div class="column">
        </div>

    </div>
  
  <div class="columns is-multiline">
    <!-- <div class="column ">
      
    </div> -->
    <div class="column is-full">
      <div class="container">
        <h4 class="title">Skills</h4>
        <p class="subtitle">Alguna de las Skills que utilizo para desarrollar</p>
      </div>
      <div class="container-tools">
          <div class="box-tools">
          <i class="devicon-django-plain"></i>
        </div>
        <div class="box-tools">
          <i class="devicon-html5-plain"></i>
        </div>
        <div class="box-tools">
          <i class="devicon-css3-plain"></i>
        </div>
        <div class="box-tools">
          <i class="devicon-python-plain"></i>
        </div>
        <div class="box-tools">


          <i class="devicon-linux-plain"></i>
                    

        </div>
          
      </div>
    </div>
    <!-- <div class="column">Auto</div>
  </div> -->
</section>

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

  p {
    font-family: "Inconsolata", monospace;
    line-height: 1.25rem;
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
    height: 200px;
  }

  
  .box-tools{
    margin: 10px;
    height: 75px;
    width: auto;
    
  }
  .box-tools i{
    font-size: 70px;
  }
</style>
