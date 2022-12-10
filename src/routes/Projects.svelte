<script>
  import { onMount } from "svelte";
  let projects = [];

  onMount(async () => {
    fetch("http://127.0.0.1:8000/project/")
      .then((response) => response.json())
      .then((data) => {
        projects = data;
        console.log(projects);
        // console.log(data);
      })
      .catch((error) => {
        console.log(error);
        return [];
      });
  });
</script>

<section class="hero is-fullheight">
  <div class="hero-body">
    <div class="container is-fluid">
      <div class="columns is-multiline">
        {#each projects as project}

        <div class="column is-full" >
          <div class="container-project">
            <div class="container-img" >
              <img class="" src="{project.pro_img}" alt="Placeholder image" />
            </div>
			<div class="container-info" >
				<h4>{project.name}</h4>
				<p>{project.description}</p>


        <div class="container-tecno">
          
          <i class="devicon-django-plain"></i>
          <i class="devicon-html5-plain"></i>
          <i class="devicon-javascript-plain"></i>
          <i class="devicon-css3-plain"></i>
          

                    
        </div>
				<div class="container-code" >
          <a href="{project.link_repo}">
          <button class="button buttom-color">
            <span class="icon">
              <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png"/>
            </span>
            <span>GitHub</span>
          </button>
        </a>
        <a href="{project.link_live}">
          <button class="button buttom-color">

            <span class="icon">
              <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png"/>
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
  </div>
</section>

<style>
  .hero {
    background-color: #0f0e17;
  }

  .container-project{
	display: flex;
	flex-direction: row;
	justify-content: center;
	align-items: center;
	flex-wrap: wrap;
  }


  .container-img{
	margin: 8px;
	width: 600px;
  }

  .container-info{
	margin: 8px;
	text-align: center;
	width: 682px;
  }

  .container-info h4{
	font-size: 36px;
    font-family: "Inconsolata", monospace;
	color: #fffffe;
  }

  .container-info p{
	line-height: 1.25rem;
	color: #a7a9be;

  }

  .container-code{
    margin: 16px;
  }

  .container-tecno{
    display: flex;
    flex-direction: row;
    justify-content: center;
    height: 30px;
    margin: 16px;
  }
  .container-tecno i{
    font-size: 16px;
    margin: 4px;
  }

  .buttom-color{
    background-color: #ff8906;
    color: #fffffe;
  }
</style>
