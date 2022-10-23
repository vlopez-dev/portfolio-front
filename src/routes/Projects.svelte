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
          <button class="button">
            <span class="icon">
              <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png"/>
            </span>
            <span>GitHub</span>
          </button>
        </a>
        <a href="{project.link_live}">
          <button class="button">

            <span class="icon">
              <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png"/>
            </span>
            <span>Demo</span>

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
    background-color: #fced73;
  }

  .container-project{
	display: flex;
<<<<<<< HEAD
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
	color: #363636;
  }

  .container-info p{
	line-height: 1.25rem;
	color: #363636;

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
</style>
=======
	align-items: flex-end;
	transition: 0.4s ease-out;
  -webkit-box-shadow: 5px 5px 15px 5px #000000; 
  box-shadow: 5px 5px 15px 5px #000000;

}

.card:hover{
  transform: translateY(20px);

}

.card::before{
  opacity: 0.3;

}

.info{
  opacity: 1;
	transform: translateY(0px);
}

.card::before{
    content: "";
		position: absolute;
		top: 0;
		left: 0;
		display: block;
		width: 100%;
		height: 100%;
		border-radius: 15px;
		background: rgba(black, 0.6);
		z-index: 2;
		transition: 0.5s;
		opacity: 0;
}
   
img{
    width: 100%;
		height: 100%;
		object-fit: cover;
		position: absolute;
		top: 0;
		left: 0;
		border-radius: 15px;
}


.info{
    position: relative;
		z-index: 3;
		color: white;
		opacity: 0;
		transform: translateY(30px);
		transition: 0.5s;
}

.info h2{
  margin: 0px;

}

.info p{
      letter-spacing: 1px;
			font-size: 15px;
			margin-top: 8px;
}
		
.info button{
      padding: 0.6rem;
			outline: none;
			border: none;
			border-radius: 3px;
			background: white;
			color: black;
			font-weight: bold;
			cursor: pointer;
			transition: 0.4s ease;
}

.info button:hover{
  background: dodgerblue;
	color: white;
}



</style>
>>>>>>> d4ac3dce7ea8b56c8da46b5ddcdb6379c0461de7
