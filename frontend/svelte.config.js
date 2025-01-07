


import adapter from "@sveltejs/adapter-node";

/** @type {import('@sveltejs/kit').Config} */
const config = {
    kit: {
        adapter: adapter({
            out: 'build', // Directorio de salida
            precompress: false, // Precomprimir archivos
            env: {
                host: '0.0.0.0',
                port: process.env.PORT || 5173
            }
        })
    }
};

export default config;
