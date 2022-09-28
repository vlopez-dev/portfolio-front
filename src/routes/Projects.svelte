<script>
  import { onMount } from "svelte";
  const projects=[]

  onMount(async () => {
  fetch("http://127.0.0.1:8000/project/")
  .then(response => response.json())
  .then(data => {
    data = projects
		console.log(data);
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
      <div class="card">
        <figure class="image is-4by3">
          <img src="https://images.unsplash.com/photo-1660308985375-bf5984ff786e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1121&q=80" alt="Placeholder image">
        </figure>
        <!-- {#each projects as poject}
          <p style="color:black">{project.name}</p>
        {/each} -->
      </div>
      
    </div>
    <div class="column">
      <div class="card">
        <figure class="image is-4by3">
          <img src="https://images.unsplash.com/photo-1660068183020-616529579fce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80">
        </figure>
      </div>
    </div>
    <div class="column">

      <div class="card">
        <figure class="image is-4by3">
          <img src="https://images.unsplash.com/photo-1531581147762-5961e6e2e6b1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80">
        </figure>
      </div>
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