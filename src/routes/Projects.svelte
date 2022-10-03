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
          <img src="{project.pro_img}" alt="Placeholder image">
        </figure>
        <div class="card-content">
          <div class="content">
            <p style="color:black">{project.name}</p>

            <p>{project.description}</p>
          </div>
        </div>
        <footer class="card-footer">
          <p class="card-footer-item">
            <span>
              View on <a href="https://twitter.com/codinghorror/status/506010907021828096">Twitter</a>
            </span>
          </p>
          <p class="card-footer-item">
            <span>
              Share on <a href="#">Facebook</a>
            </span>
          </p>
        </footer>

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

  
</style>