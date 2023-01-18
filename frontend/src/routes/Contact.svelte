<script>
    import Animate from "./Animate.svelte";


</script>




<Animate>
  <section class="hero is-fullheight  " >
    <div class="columns is-multiline ">
      <div class="column"></div>
      <div class="column is-one-third m-6">
        <form class="mt-6" action="">
        <div class="field">
          <label class="label">Email</label>
          <div class="control has-icons-left has-icons-right">
            <input class="input is-danger" type="email" placeholder="Email input" value="hello@">
            <span class="icon is-small is-left">
              <i class="fas fa-envelope"></i>
            </span>
            <span class="icon is-small is-right">
              <i class="fas fa-exclamation-triangle"></i>
            </span>
          </div>
          <p class="help is-danger">This email is invalid</p>
        </div>
        <div class="field">
          <label class="label">Message</label>
          <div class="control">
            <textarea class="textarea" placeholder="Textarea"></textarea>
          </div>
        </div>
        
    
     
        
        <div class="field is-grouped">
          <div class="control">
            <button class="button is-link">Send</button>
          </div>
         
        </div>
      </form>
      </div>
      
      <div class="column"></div>

    </div>
  </section>
</Animate>







  <style>
   
   section{
    background-color: #0f0e17;
   }

   .title{
    font-family: 'Karla', sans-serif;

   }

   p{
    font-family: 'Inconsolata', monospace;
    line-height: 1.25rem;
    color: #363636;
   }
   
  </style>