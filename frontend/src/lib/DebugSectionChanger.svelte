<script>
  import { currentSection, sectionColors } from './stores.js';

  function changeSection(section) {
    console.log('🔄 Cambiando manualmente a:', section);
    currentSection.set(section);
  }
</script>

<!-- Panel de debug temporal -->
<div style="position: fixed; top: 100px; right: 20px; z-index: 9999; background: rgba(0,0,0,0.8); padding: 15px; border-radius: 8px; color: white; font-size: 12px;">
  <h4 style="margin: 0 0 10px 0; color: #FFB6B9;">🔧 Debug Panel</h4>
  <p style="margin: 5px 0;">Sección: <strong>{$currentSection}</strong></p>
  
  <div style="display: flex; flex-direction: column; gap: 5px; margin-top: 10px;">
    <button on:click={() => changeSection('home')} 
            style="padding: 5px 10px; background: #FFF0F5; color: #2B2D42; border: none; border-radius: 4px; cursor: pointer;">
      Home
    </button>
    <button on:click={() => changeSection('about')} 
            style="padding: 5px 10px; background: #EDE7F6; color: #3E3A4D; border: none; border-radius: 4px; cursor: pointer;">
      About
    </button>
    <button on:click={() => changeSection('projects')} 
            style="padding: 5px 10px; background: #E0F7FA; color: #004D40; border: none; border-radius: 4px; cursor: pointer;">
      Projects
    </button>
    <button on:click={() => changeSection('contact')} 
            style="padding: 5px 10px; background: #FFF9C4; color: #5D4037; border: none; border-radius: 4px; cursor: pointer;">
      Contact
    </button>
  </div>
</div>