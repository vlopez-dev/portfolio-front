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

      <div class=" card__fig card-image">

        <figure class="image is-4by3">
          <figcaption>
            
          <img class="card__image" src="{project.pro_img}" alt="Placeholder image">
          <div class="info">
            <h2>{project.title}</h2>
            <p>{project.description}</p>
          </div>
          </figcaption>
        </figure>
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

.card__fig{
  border-radius: 15px;
	padding: 1.5rem;
	background: white;
	position: relative;
	transition: 0.4s ease-out;
	box-shadow: 0px 7px 10px rgba(black, 0.5);

}

.card__fig:hover{
  transform: translateY(20px);

}

.card__fig::before{
  opacity: 1;

}

.info{
  opacity: 1;
	transform: translateY(0px);
}

.info::before{
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
</style>