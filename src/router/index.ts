import { createRouter, createWebHistory } from 'vue-router'
import PageHome from '@/PageHome.vue'
import PageProjects from '@/PageProjects.vue'
import PageSkills from '@/PageSkills.vue'
import PageWhoami from '@/PageWhoami.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: PageHome, name: 'Home' },
    { path: '/about', component: PageWhoami, name: '$(whoami?)' },
    { path: '/projects', component: PageProjects, name: 'Projects' },
    { path: '/skills', component: PageSkills, name: 'Skills' },
  ],
})

export default router
