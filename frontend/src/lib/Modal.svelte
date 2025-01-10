
<script>
    import { onMount } from "svelte";
    
    export let showModal
    
  function clickModal(event){
    event.preventDefault();
    showModal = true;
    console.log("Ejecute click Modal")
    console.log(showModal)
  }


  function closeModal(){
    showModal=false;
  }
   

    onMount(() => {
    console.log('Componente Modal montado correctamente');
  });

</script>



<div class="modal {showModal ? 'is-active' : ''}">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Modal title</p>
        <button class="delete" aria-label="close"></button>
      </header>
      <section class="modal-card-body">
        <!-- Content ... -->
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success">Save changes</button>
        <button on:click={closeModal} class="button">Cancel</button>
      </footer>
    </div>
  </div>




<style>

</style>