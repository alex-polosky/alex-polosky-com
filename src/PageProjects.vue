<script setup lang="ts">
import { ref } from 'vue'
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

interface PortDatum {
  title: string
  blurb: string
  desc?: string
  images: {
    title: string
    path: string
    caption: string
  }[]
}

const DATA = ref<PortDatum[]>([
  {
    title: 'DSCSA Solution Platform',
    blurb:
      'The pharmaceutical supply chain has a need for compliant tracking.\nThis platform enabled manufacturers to both be compliant and have control over their data.',
    // desc: '',
    images: [
      {
        title: 'Home',
        path: 'dscsa/0.dashboard.png',
        caption: 'The dashboard home page',
      },
      {
        title: 'Inbox',
        path: 'dscsa/1.inbox.png',
        caption: 'Your inbox, where all of your incoming messages live',
      },
      {
        title: 'Recall',
        path: 'dscsa/2.notifications.png',
        caption: 'A list of all of your recall messages',
      },
      {
        title: 'Slides',
        path: 'dscsa/3.multiple-slides.png',
        caption: 'Showing off multiple slides and the drop down editor',
      },
      {
        title: 'Status',
        path: 'dscsa/4.de-status.png',
        caption: 'All of your incoming and outgoing files that are processed',
      },
      {
        title: 'Filters',
        path: 'dscsa/5.filters.png',
        caption: 'Editable filters to drill down the status of the files',
      },
      {
        title: 'Map 1',
        path: '/dscsa/6.dispensers.png',
        caption: 'Snapshot of clustered view of dispensers for use with Dropship',
      },
      {
        title: 'Map 2',
        path: '/dscsa/7.dispensers.png',
        caption: 'Snapshot of zoomed in view of dispensers for use with Dropship',
      },
    ],
  },
  {
    title: 'Club Card by Futures',
    blurb:
      'An app that would allow users to purchase and pay for drinks at bars or other establishments.\nCustomers could open tabs and close them out, along with tips, all from their phone.',
    images: [
      {
        title: '',
        path: 'clubcard/1.login.jpg',
        caption: 'The login page',
      },
      {
        title: '',
        path: 'clubcard/2.bar_list.jpg',
        caption: 'A map and list of nearby establishments',
      },
      {
        title: '',
        path: 'clubcard/3.list_drinks_plus_ad.jpg',
        caption: 'Listing of drinks',
      },
      {
        title: '',
        path: 'clubcard/4.order_drink.jpg',
        caption: 'Details of a drink, before ordering',
      },
      {
        title: '',
        path: 'clubcard/5.submitted.jpg',
        caption: 'Successful ordering',
      },
      {
        title: '',
        path: 'clubcard/6.notification.jpg',
        caption: 'Push notification of placed order',
      },
      {
        title: '',
        path: 'clubcard/7.selecting_tab.jpg',
        caption: 'Side menu for a logged in user',
      },
      {
        title: '',
        path: 'clubcard/8.notification_and_tab.jpg',
        caption: "A user's tab",
      },
      {
        title: '',
        path: 'clubcard/9.tab_buttons.jpg',
        caption: 'Users could only mark a drink received once an employee marked it ready',
      },
      {
        title: '',
        path: 'clubcard/db.all.png',
        caption: 'The full database schema and relations of the project',
      },
      {
        title: '',
        path: 'clubcard/db.inv.png',
        caption: 'The database schema for the inventory system',
      },
      {
        title: '',
        path: 'clubcard/db.users.png',
        caption: 'The schema for users',
      },
    ],
  },
  {
    title: 'IEM System',
    blurb:
      'As an avid local musician and tech nerd, I had a drive to build an In-Ear-System.\nThis allowed several musicians to plug in, and I would mix the sound for both front of house and up to 6 musicians.',
    images: [
      {
        title: '',
        path: 'iem/20230123_181921.jpg',
        caption: 'The back-end, featuring the mixer, power board, router, and external connections',
      },
      {
        title: '',
        path: 'iem/20230123_182102.jpg',
        caption:
          'The front-end, showing where each mic / instrument would plug into, as well as controls for the wireless units',
      },
      {
        title: '',
        path: 'iem/20230123_182330.jpg',
        caption: 'The full system on display',
      },
      {
        title: '',
        path: 'iem/20230123_183201.jpg',
        caption: "The mess of front-end cables I'd use for connecting mics and instruments",
      },
      {
        title: '',
        path: 'iem/20230123_183810.jpg',
        caption:
          'These were primarily used for connecting the drummer into the system, utilizing both forward/backward connects for in-ears and mics',
      },
      {
        title: '',
        path: 'iem/20230123_185357.jpg',
        caption: 'The mixer program I would use for mixing at venues',
      },
    ],
  },
])

const GITHUB = ref([
  {
    link: 'ttrpg-audio-scene',
    text: 'An attempt to create an audio file browser / player sound board to make TTRPG game mastering more fun',
  },
  {
    link: 'pygic-the-conjuring',
    text: 'The start of a Magic the Gathering card parser and rules engine.',
  },
  {
    link: 'complex-math-calculator',
    text: 'A complex binary (-1 + i) calculator, written in angular. Support for decimals and arbitrary precision.\nWill eventually be visible at: https://alex-polosky.github.io/complex-math-calculator/',
  },
  {
    link: 'django-microservice-template',
    text: 'Github template repo to help make microservices easily',
  },
  {
    link: 'genecos-experiment',
    text: 'Fun demo Django project showcasing client contract mapping',
  },
  {
    link: 'live-xslt',
    text: 'A live XSLT editor; handy for editing XSLTs with live XML data',
  },
  {
    link: 'pygame-sigil',
    text: 'This was an attempt (in 2014) to make a gaming library on top of PyGame a la Unreal or Unity. It wasnt very serious',
  },
  {
    link: 'EntityEngine',
    text: 'This was another attempt (in 2016) to make a gaming engine on top of SharpDX in C#, also similar to Unreal or Unity. It had support for scripting in Python rather than Lua or C#. Was slightly more serious, but never finished',
  },
])
</script>

<template>
  <p>Hi there! This is a collection of some projects I've worked on</p>
  <p>
    Currently I'm using
    <a href="https://antoniandre.github.io/vueper-slides/" target="_blank">vueper slides </a> to
    drive these as I want to get this page working
  </p>
  <p>
    This site itself is a
    <a href="https://github.com/alex-polosky/alex-polosky-com" target="_blank">project</a> made
    using Vue, and is an upgrade from my
    <a href="https://github.com/alex-polosky/alex-polosky-info" target="_blank">last site</a> which
    used angular.
  </p>
  <p>
    I've got a few random repos of projects that I've attempted in my spare time, which can be found
    here:
  </p>
  <dl>
    <template v-for="(data, index) of GITHUB" :key="index">
      <dt>
        <a :href="`https://github.com/alex-polosky/${data.link}`" target="_blank">{{
          data.link
        }}</a>
      </dt>
      <dd>
        {{ data.text }}
      </dd></template
    >
  </dl>
  <template v-for="(data, index) in DATA" :key="index">
    <hr />
    <h2>{{ data.title }}</h2>
    <p>{{ data.blurb }}</p>
    <vueper-slides :slide-ratio="1 / 2" :slide-content-outside="'bottom'">
      <vueper-slide
        v-for="(slide, i) in data.images"
        :key="i"
        :title="`<h3>${slide.title}</h3>`"
        :content="`<p>${slide.caption}</p><a href='portfolio/${slide.path}' target='_blank'>View Image</a>`"
        :image="`portfolio/${slide.path}`"
      ></vueper-slide>
    </vueper-slides>
  </template>
</template>

<style scoped>
a {
  color: #5ecdf0;
}
</style>
