<script>
  import Carousel from 'svelte-carousel';
  import { onMount } from "svelte";

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

  let certificates = [];

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

  let loaded = [];

function handleLoad(index) {
  loaded = [...loaded, index];
}






</script>
<Carousel let:loaded {options}>
  {#each certificates as certificate, certificateIndex (certificate)}
    <div class="img-container" >
      {#if loaded.includes(certificateIndex)}
        <img src="{certificate.imagecert}" alt="Certificado" on:load={(event) => handleLoad(certificateIndex)} />
      {/if}
    </div>
  {/each}
</Carousel>
<style>

</style>