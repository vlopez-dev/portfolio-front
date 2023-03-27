<script>
  import Carousel from 'svelte-carousel';
  import { onMount } from "svelte";
  import { slide } from "svelte/transition";

  let certificates = [];
  let currentSlide = 0;
  
  onMount(async () => {
    fetch("http://127.0.0.1:8001/certificates/")
      .then((response) => response.json())
      .then((data) => {
        certificates = data;
        console.log(certificates);
        console.log(data);
      })
      .catch((error) => {
        console.log(error);
        return [];
      });
  });

  const nextImage = () => {
    currentSlide += 1;
  };


  const prevImage = () => {
    currentSlide -= 1;
  };




</script>

<Carousel
let:loaded
>
  {#if certificates.length === 0}
    <div>No images to show</div>
  {:else}
    {#each certificates as certificate}
      <img
        transition:slide
        src={certificate.imagecert}
        alt={certificate.title}
        width={400}
        height={300}
      />
    {/each}
  {/if}
</Carousel>





<style>

</style>