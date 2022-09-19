<script>
    export let hero_title,hero_subtitle,hero_image
</script>

<section class="hero  is-fullheight">
    <div class="hero-body">
      <div class="">
        <p class="title">
            {hero_title}
        </p>
        <p class="subtitle">
            {hero_subtitle}
        </p>
      </div>
    </div>
  </section>

  <style>
   .hero{
    background-color: #f4dd24;
   }
    .hero-body{
        justify-content: center;
    }
  </style>