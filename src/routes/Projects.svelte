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
  <div class="columns">
    <div class="column">
      {#each projects as project}

      <div class="card">
        <figure class="image is-4by3">
          <img src="{project.pro_img}" alt="Placeholder image">
        </figure>
          <p style="color:black">{project.name}</p>
          <p>{project.description}</p>
      </div>
      {/each}

    </div>
  

  </div>
</div>
</div>
  </section>







<style>
.hero{
    background-color: #fced73;
   }
</style>