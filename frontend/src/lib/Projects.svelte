<script>
  import { GithubIcon,CloudIcon,InfoIcon } from 'svelte-feather-icons'
  import Modal from './Modal.svelte';

  import { onMount } from "svelte";
  

  let showModal
  
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
        // console.log(error);
        return [];
      });
  });

</script>

<section class="hero is-fullheight projects-section">
    <div class="container is-fluid">
      <div class="columns is-multiline mx-2 my-6 ">
        {#each projects as project}

        <div class="column is-full" >
          <div class="container-project m-auto">
            <div class="container-img" >
              <img class="" src="{project.pro_img}" alt="Placeholder image" />
            </div>
			<div class="container-info" >
				<h4 class="custom-title">{project.name}</h4>
				<p class="paragraph custom-text">{project.description}</p>


        <div class="custom-container-tecno">

          {#each project.technologys as technology}
            <i class={technology.icon}></i>
          {/each}
        </div>
				<div class="container-code" >
          <a href="{project.link_repo}" target=”_blank”>
          <button class="button  custom-buttom-color  is-normal is-rounded">
            <span class="icon ">
              <GithubIcon size="24" />
            </span>
            <span>GitHub</span>
          </button>
        </a>
        <a href="{project.link_live}" target=”_blank”>
          <button class="button  custom-buttom-color is-normal is-rounded">

            <span class="icon">
              <CloudIcon size="24" />

            </span>
            <span>Live</span>

          </button>
        </a>

<!--        
          <button   on:click={() => { showModal = true;  }} class="button  custom-buttom-color is-normal is-rounded">

            <span class="icon">
              <InfoIcon size="24" />

            </span>
            <span>Info</span>

          </button> -->
<!-- 
        <Modal {showModal}
        ></Modal> -->
				  </div>
			  </div>
			</div>
			        </div>

        {/each}
      </div>
    </div>
</section>

<style>


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


  .container-code{
    margin: 12px;
  }

  .custom-container-tecno i{
    font-size: 16px;
    margin: 4px;
  }


  .paragraph{
    text-align: center;
    padding: 16px;
    font-family: "Inconsolata", monospace;
    line-height: 1.25rem;
    color: #a7a9be;
  }






.custom-title{
  font-size: 36px;
    font-family: "Inconsolata", monospace;
	color: #1f1235;
}



:global(body.dark-mode) .custom-title {
        color: #f0f0f0;
}



.custom-buttom-color{
  background-color: #ff6e6c;
  width: 105px;
  color: #fffffe;
  border: none;
  }



:global(body.dark-mode) .custom-buttom-color {
        color: #f0f0f0;
        width: 105px;

        background-color: #ff8906;

}




.custom-container-tecno{
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
    color:white

}

.projects-section {
  background-color: #E0F7FA;
  color: #004D40;
  transition: background-color 0.4s cubic-bezier(0.4, 0, 0.2, 1);
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
  color: #00796B;
}

.paragraph {
  text-align: center;
  padding: 16px;
  font-family: "Inconsolata", monospace;
  line-height: 1.25rem;
  color: #006064;
}

.custom-title {
  font-size: 36px;
  font-family: "Inconsolata", monospace;
  color: #004D40;
}

.custom-buttom-color {
  background-color: #80DEEA;
  width: 105px;
  color: #004D40;
  border: none;
}

/* Modo oscuro */
:global(body.dark-mode) .projects-section {
  background-color: #004D40;
  color: #E0F7FA;
}

:global(body.dark-mode) .custom-title,
:global(body.dark-mode) .paragraph {
  color: #E0F7FA;
}

:global(body.dark-mode) .custom-container-tecno i {
  color: #E0F7FA;
}

:global(body.dark-mode) .custom-buttom-color {
  background-color: #26C6DA;
  color: #E0F7FA;
  box-shadow: 0 0 10px rgba(38, 198, 218, 0.4);
}





</style>
