<script>
    export let about_title,about_description,src
    

</script>
<section class="hero is-fullheight " >
  <div class="hero-body">
  <div class="columns">
    <div class="column" >
    </div>
    <div class="column">
      <img src="https://images.unsplash.com/photo-1499155286265-79a9dc9c6380?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=684&q=80" alt="">
    </div>
    <div class="column" >
    </div>
    <div class="column" >
      <h2 class="title">Titulo</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ullam dolores ipsum, sapiente veritatis totam reiciendis eveniet. Aliquam aliquid eius magnam quas, accusamus nemo ratione, laborum quaerat, quasi adipisci neque earum.</p>
      <button>CV</button>
    </div>
    
  </div>
</div>
</section>


  <section class="hero is-fullheight  timeline-wrapper">
    <div class="columns" style="outline: 2px solid red">
      <div class="column"></div>
      <div class="column">
    <div class="middle-line"></div>

    <div class="box box-top">
        <div class="date">
            <p>20</p>
            <p>DEC</p>
        </div>
        <div class="box-content">
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod</p>
        </div>
    </div>

    <div class="box box-bottom">
        <div class="date">
            <p>11</p>
            <p>AUG</p>
        </div>
        <div class="box-content">
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod</p>
        </div>
    </div>
  </div>
  <div class="column"></div>
  <div class="column"></div>

  </div>
</section>



  <style>
   
   section{
    background-color: #fced73;
   }

   .title{
    font-family: 'Karla', sans-serif;

   }

   p{
    font-family: 'Inconsolata', monospace;
    line-height: 1.25rem;
    color: #363636;
   }

   

   .timeline-wrapper {
  /* position: relative; */
  width: 100%;
  margin: auto;
  height: 300px;
}


.timeline-wrapper {
  /* position: relative; */
  width: 100%;
  margin: auto;
  height: 300px;
}

.box {
  width: 17%;
  /* position: relative; */
  min-height: 300px;
  float: right;
}


.box .date {
  /* position: absolute; */
  top: 50%;
  left: 0px;
  transform: translateY(-50%);
  width: 50px;
  height: 50px;
  border-radius: 100%;
  background: #fff;
  border: 2px solid #d9d9d9;
}
.date p {
  text-align: center;
  margin-top: 3px;
  margin-bottom: 0px;
}
   
  </style>