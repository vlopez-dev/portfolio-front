<script>
import { GithubIcon,LinkedinIcon,TwitterIcon } from 'svelte-feather-icons'

</script>

<footer class="footer m-auto custom-component ">
    <div class="content has-text-centered">
      <p>
       
      </p>
      <div class="social">
        <div class="box_social custom-icons">
          <a href="https://twitter.com/vic_mde" class="custom-icons" target="_blank">
          <TwitterIcon size="24" />
        </a>
        </div>
        <div class="box_social custom-icons">
          <a href="https://github.com/vlopez-dev" class="custom-icons" target="_blank">
          <GithubIcon size="24" />
        </a>
        </div>
        <div class="box_social custom-icons">
          <a href="https://www.linkedin.com/in/victorlopezr/" class="custom-icons" target="_blank">
          <LinkedinIcon size="24" />
        </a>
        </div>
        


      </div>
      
    </div>
  </footer>

  <style>
    .footer{
        height: 80px;
        width: 100%;
        background-color: #0f0e17;
    }

    a{
        color: #a7a9be;
        font-family: 'Karla', sans-serif;
        padding: 10px;

    }
    p{
        color: #a7a9be;
        font-family: 'Karla', sans-serif;

    }

    .social{
      display: flex;
      flex-direction: row;
      justify-content: center;
      height: auto;
      width: auto;
    }


    .social a{
      padding: 2px;
    }


    .box_social{
      margin: 10px;
    }




    



    .custom-icons {
      color: black;
      
    }


    


:global(body.dark-mode) .custom-icons {
        background-color: #0f0e17;
        color: #fffffe;
    }





    .footer {
  height: 80px;
  width: 100%;
  background-color: #FFEBE5;
}

a,
p {
  color: #5D4037;
  font-family: 'Karla', sans-serif;
  padding: 10px;
}

.social {
  display: flex;
  flex-direction: row;
  justify-content: center;
  height: auto;
  width: auto;
}

.social a {
  padding: 2px;
}

.box_social {
  margin: 10px;
}


.custom-icons {
  color: #5D4037;
  transition: color 0.3s ease;
}

.custom-icons:hover {
  color: #FFB6B9;
}

/* Modo oscuro */
:global(body.dark-mode) .footer {
  background-color: #3E3A4D;
}


:global(body.dark-mode) a,
:global(body.dark-mode) p,
:global(body.dark-mode) .custom-icons {
  color: #FFF9C4;
}

:global(body.dark-mode) .custom-icons:hover {
  color: #FFB6B9;
}


  </style>