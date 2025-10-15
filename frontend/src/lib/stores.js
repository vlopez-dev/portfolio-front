import { writable } from 'svelte/store';

// Store para la sección actualmente visible
export const currentSection = writable('home');

// Colores para cada sección - Modo claro
export const sectionColors = {
  home: {
    bg: '#FFF0F5',
    text: '#2B2D42',
    accent: '#FFB6B9',
  },
  about: {
    bg: '#EDE7F6',
    text: '#3E3A4D',
    accent: '#D4C5F9',
  },
  projects: {
    bg: '#E0F7FA',
    text: '#004D40',
    accent: '#B2E5E7',
  },
  contact: {
    bg: '#FFF9C4',
    text: '#5D4037',
    accent: '#FFD54F',
  },
};

// Colores para cada sección - Modo oscuro
export const sectionColorsDark = {
  home: {
    bg: '#2B2D42',
    text: '#F7F7F7',
    accent: '#D4C5F9',
  },
  about: {
    bg: '#3E3A4D',
    text: '#EDE7F6',
    accent: '#FFB6B9',
  },
  projects: {
    bg: '#004D40',
    text: '#E0F7FA',
    accent: '#B2E5E7',
  },
  contact: {
    bg: '#5D4037',
    text: '#FFF9C4',
    accent: '#FFD54F',
  },
};

// Store para el modo oscuro
export const darkMode = writable(false);
