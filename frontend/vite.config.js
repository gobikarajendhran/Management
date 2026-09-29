import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { VitePWA } from 'vite-plugin-pwa'
export default defineConfig({
  plugins: [react(), VitePWA({registerType:'autoUpdate', includeAssets:['icon.svg'], manifest:{name:'Kavish Business Management',short_name:'Kavish Business',description:'Internal business management app',theme_color:'#0f172a',background_color:'#f8fafc',display:'standalone',start_url:'/',icons:[{src:'/icon.svg',sizes:'any',type:'image/svg+xml',purpose:'any maskable'}]}})],
  server:{port:5173,host:'localhost'}
})
