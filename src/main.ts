import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

console.log('main.ts: Script loaded')

const app = createApp(App)

// Global error handler
app.config.errorHandler = (err, _instance, info) => {
  console.error('Vue error:', err, info)
  // Don't prevent app from mounting
}

app.use(createPinia())
app.use(router)

console.log('main.ts: About to mount app')
app.mount('#app')
console.log('main.ts: App mounted')
