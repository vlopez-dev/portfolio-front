<script>
  import { onMount } from "svelte";
  let projects=[]

  onMount(async () => {
  fetch("http://127.0.0.1:8000/project/")
  .then(response => response.json())
  .then(data => {
    projects=data
    console.log(projects)
		// console.log(data);
  }).catch(error => {
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

    <div class="column is-one-quarter-desktop is-half-tablet">

      <div class="card-image">

        <figure class="image is-4by3">
          <figcaption class="card__caption">

          <img class="card__image" src="{project.pro_img}" alt="Placeholder image">
            <h2>{project.title}</h2>
            <p>{project.description}</p>
          </figcaption>
        </figure>
        <!-- <div class="card-content">
          <div class="content">
            <p style="color:black">{project.name}</p>

            <p>{project.description}</p>
          </div>
        </div> -->
    

      </div>

    </div>

    {/each}

  </div>

</div>
</div>
  </section>







<style>
.hero{
    background-color: #fced73;
   }

   .card__image {
			transform: translateY(-10px);
      
		}




		.card__caption :hover{
			top: 50%;
			transform: translateY(-50%);
      background: linear-gradient(0deg, rgba(0, 0, 0, .5) 40%, rgba(255, 255 ,255 , 0) 100%);
			transition: .3s;
		}

</style>