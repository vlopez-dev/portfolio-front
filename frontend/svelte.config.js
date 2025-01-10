import adapter from '@sveltejs/adapter-node';

export default {
  kit: {
    adapter: adapter({
      out: 'build',
      precompress: false,
      env: {
        host: '0.0.0.0',
        port: process.env.PORT || 4173
      }
    })
  }
};