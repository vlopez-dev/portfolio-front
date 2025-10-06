<script>
import { GithubIcon,LinkedinIcon,TwitterIcon } from 'svelte-feather-icons';
import { currentSection, sectionColors, sectionColorsDark, darkMode } from './stores.js';

let currentColors = sectionColors.contact; // default

// Reactivity - actualizar colores cuando cambie la sección
$: currentColors = $darkMode ? sectionColorsDark[$currentSection] : sectionColors[$currentSection];

// Debug: observar cambios  
$: console.log('🦶 Footer - Sección actual:', $currentSection, 'Colores:', currentColors);

</script>

<footer class="footer m-auto custom-component" 
         style="--current-bg: {currentColors?.bg || '#FFF9C4'}; --current-text: {currentColors?.text || '#5D4037'}; --current-accent: {currentColors?.accent || '#FFB6B9'}">
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
    .footer {
      height: 80px;
      width: 100%;
      background-color: var(--current-bg);
      box-shadow: 0 -1px 8px rgba(255, 182, 185, 0.1);
      border-top: 1px solid rgba(255, 182, 185, 0.2);
      backdrop-filter: blur(8px);
      position: relative;
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    a,
    p {
      color: var(--current-text);
      font-family: 'Karla', sans-serif;
      padding: 10px;
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .social {
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      height: auto;
      width: auto;
    }

    .social a {
      padding: 8px;
      border-radius: 50%;
      transition: all 0.3s ease;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .social a:hover {
      background-color: var(--current-accent);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(255, 182, 185, 0.2);
    }

    .box_social {
      margin: 8px;
    }

    .custom-icons {
      color: var(--current-text);
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .custom-icons:hover {
      color: white;
      transform: scale(1.1);
    }

    /* Modo oscuro */
    :global(body.dark-mode) .footer {
      background-color: #5D4037;
      border-top: 1px solid rgba(212, 197, 249, 0.2);
      box-shadow: 0 -1px 8px rgba(212, 197, 249, 0.1);
    }

    :global(body.dark-mode) a,
    :global(body.dark-mode) p {
      color: #FFF9C4;
    }

    :global(body.dark-mode) .custom-icons {
      color: #FFF9C4;
    }

    :global(body.dark-mode) .custom-icons:hover {
      color: white;
    }

    :global(body.dark-mode) .social a:hover {
      background-color: #FFB6B9;
    }
  </style>
