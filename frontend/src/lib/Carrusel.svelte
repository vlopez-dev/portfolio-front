<script>
  import Carousel from 'svelte-carousel';
  import { slide } from "svelte/transition";

  export let certificates = [];
  
  let options = {
    autoplay: true,
    autoplaySpeed: 3000,
    arrows: false,
    dots: true,
    infinite: true,
    slidesToShow: 2,
    slidesToScroll: 2,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
    ],
  };

  let loaded = [];
  let i=[];
  function handleLoad(index) {
    loaded = [...loaded, index];
  }

</script>

<Carousel let:loaded {options}>

  {#if certificates.length === 0}
    <div>No images to show</div>
  {:else}
    {#each certificates as certificate,i}
      <img
        transition:slide
        src={certificate.imagecert}
        alt={certificate.title}
        width={400}
        height={300}
        on:load={(event) => handleLoad(i)}
      />
    {/each}
  {/if}
</Carousel>

<style>
  .img-container {
    height: 200;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .img-container img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
  }
</style>
