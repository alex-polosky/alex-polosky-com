<script setup lang="ts">
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

const DATA: PortDatum[] = [
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
]
</script>

<template>Filling this page out</template>

<style scoped></style>
