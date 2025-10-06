<script>
  import { onMount } from 'svelte';
  import { currentSection } from './stores.js';

  let observer;
  
  onMount(() => {
    console.log('🔍 SectionObserver iniciado');
    
    // Esperar un poco para que el DOM se renderice completamente
    setTimeout(() => {
      // Configurar Intersection Observer para detectar secciones visibles
      observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          console.log('👀 Observer detectó:', {
            target: entry.target.className,
            isIntersecting: entry.isIntersecting,
            intersectionRatio: entry.intersectionRatio
          });
          
          if (entry.isIntersecting && entry.intersectionRatio > 0.2) {
            // Determinar qué sección está visible basándose en la clase o ID
            let section = 'home'; // default
            
            if (entry.target.classList.contains('hero-section')) {
              section = 'home';
            } else if (entry.target.classList.contains('about-section')) {
              section = 'about';  
            } else if (entry.target.classList.contains('projects-section')) {
              section = 'projects';
            } else if (entry.target.classList.contains('contact-section')) {
              section = 'contact';
            }
            
            console.log('🎯 Cambiando a sección:', section);
            currentSection.set(section);
          }
        });
      }, {
        threshold: [0, 0.1, 0.2, 0.5],
        rootMargin: '0px'
      });

      // Observar todas las secciones
      const sections = document.querySelectorAll('.hero-section, .about-section, .projects-section, .contact-section');
      console.log('📋 Secciones encontradas:', sections.length, Array.from(sections).map(s => s.className));
      
      if (sections.length === 0) {
        console.log('⚠️ No se encontraron secciones. Probando selectores alternativos...');
        const altSections = document.querySelectorAll('section');
        console.log('📋 Secciones alternativas:', altSections.length, Array.from(altSections).map(s => ({ className: s.className, id: s.id, tagName: s.tagName })));
        
        // Probar otros selectores posibles
        const heroSections = document.querySelectorAll('[class*="hero"]');
        const aboutSections = document.querySelectorAll('[class*="about"]');
        const projectSections = document.querySelectorAll('[class*="project"]');
        const contactSections = document.querySelectorAll('[class*="contact"]');
        
        console.log('🔍 Elementos con "hero":', heroSections.length, Array.from(heroSections).map(s => s.className));
        console.log('🔍 Elementos con "about":', aboutSections.length, Array.from(aboutSections).map(s => s.className));
        console.log('🔍 Elementos con "project":', projectSections.length, Array.from(projectSections).map(s => s.className));
        console.log('🔍 Elementos con "contact":', contactSections.length, Array.from(contactSections).map(s => s.className));
      }
      
      sections.forEach(section => {
        if (observer) {
          console.log('👁️ Observando sección:', section.className);
          observer.observe(section);
        }
      });
      
      // Si no hay secciones, establecer home como default
      if (sections.length === 0) {
        console.log('🏠 Estableciendo sección por defecto: home');
        currentSection.set('home');
      }
    }, 1000);

    // Cleanup
    return () => {
      if (observer) {
        observer.disconnect();
      }
    };
  });
</script>

<!-- Este componente no renderiza nada visible -->