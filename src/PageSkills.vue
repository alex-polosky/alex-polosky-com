<script setup lang="ts">
import { computed, ref } from 'vue'

const HEADERS = ref({
  name: 'Skill',
  type: 'Category',
  level: 'Level',
})

const DATA = ref([
  { type: 'Concept', name: 'Blockchain', level: 3 },
  { type: 'Concept', name: 'Caching', level: 7 },
  { type: 'Concept', name: 'Content management systems', level: 6 },
  { type: 'Concept', name: 'Data design', level: 7 },
  { type: 'Concept', name: 'Deployment', level: 8 },
  { type: 'Concept', name: 'Distributed services', level: 7 },
  // { type: 'Concept', name: 'Document management', level: 7 },
  { type: 'Concept', name: 'Embedded systems', level: 4 },
  { type: 'Concept', name: 'Enterprise architecture', level: 7 },
  { type: 'Concept', name: 'Enterprise service bus', level: 7 },
  { type: 'Concept', name: 'Integrations', level: 9 },
  { type: 'Concept', name: 'Linux kernel', level: 2 },
  { type: 'Concept', name: 'Machine learning', level: 5 },
  { type: 'Concept', name: 'Message Queues', level: 6 },
  { type: 'Concept', name: 'Microservices', level: 8 },
  // { type: 'Concept', name: 'Networking', level: 7 },
  // { type: 'Concept', name: 'ORM', level: 8 },
  // { type: 'Concept', name: 'SEO', level: 3 },
  // { type: 'Concept', name: 'Software architecture', level: 8 },
  // { type: 'Concept', name: 'Software development', level: 9 },
  // { type: 'Concept', name: 'System administration', level: 6 },
  // { type: 'Concept', name: 'Web services', level: 8 },
  { type: 'Concept', name: 'Windows kernel', level: 2 },

  { type: 'Database', name: 'Elasticsearch', level: 4 },
  { type: 'Database', name: 'MongoDB', level: 4 },
  { type: 'Database', name: 'MSSQL', level: 6 },
  { type: 'Database', name: 'MySQL', level: 5 },
  { type: 'Database', name: 'Oracle', level: 4 },
  { type: 'Database', name: 'Postgresql', level: 7 },
  { type: 'Database', name: 'Sqlite', level: 6 },

  { type: 'Dev Ops', name: 'Active Directory', level: 4 },
  { type: 'Dev Ops', name: 'Ansible', level: 4 },
  { type: 'Dev Ops', name: 'AWS', level: 6 },
  { type: 'Dev Ops', name: 'Azure', level: 6 },
  { type: 'Dev Ops', name: 'Docker', level: 7 },
  { type: 'Dev Ops', name: 'Google Cloud Platform', level: 7 },
  { type: 'Dev Ops', name: 'Jenkins', level: 4 },
  { type: 'Dev Ops', name: 'On premise', level: 8 },
  { type: 'Dev Ops', name: 'Terraform', level: 7 },

  { type: 'Language', name: 'Assembly (6502, Z80, Custom)', level: 3 },
  { type: 'Language', name: 'C', level: 6 },
  { type: 'Language', name: 'C#', level: 8 },
  { type: 'Language', name: 'C++', level: 5 },
  { type: 'Language', name: 'CSS', level: 7 },
  // { type: 'Language', name: 'Gosu', level: 5 },
  { type: 'Language', name: 'Java', level: 6 },
  // { type: 'Language', name: 'Javascript', level: 7 },
  // { type: 'Language', name: 'JSON', level: 9 },
  { type: 'Language', name: 'Lua', level: 4 },
  // { type: 'Language', name: 'PHP', level: 5 },
  { type: 'Language', name: 'Python', level: 9 },
  { type: 'Language', name: 'Ruby', level: 4 },
  // { type: 'Language', name: 'SCSS', level: 6 },
  { type: 'Language', name: 'Typescript', level: 8 },
  // { type: 'Language', name: 'YAML', level: 7 },
  // { type: 'Language', name: 'XML', level: 8 },

  // { type: 'Library', name: 'Boost', level: 5 },
  // { type: 'Library', name: 'Dapper', level: 5 },
  // { type: 'Library', name: 'Flask', level: 7 },
  // { type: 'Library', name: 'Infragistics', level: 5 },
  // { type: 'Library', name: 'jQuery', level: 7 },

  { type: 'Management', name: 'Agile', level: 7 },
  { type: 'Management', name: 'Requirements analysis', level: 8 },
  { type: 'Management', name: 'Scrum', level: 7 },
  { type: 'Management', name: 'Technical documentation', level: 8 },

  { type: 'Package', name: '.NET Core', level: 8 },
  { type: 'Package', name: 'Angular', level: 7 },
  { type: 'Package', name: 'Cordova', level: 5 },
  { type: 'Package', name: 'Django', level: 8 },
  { type: 'Package', name: 'FastAPI', level: 7 },
  { type: 'Package', name: 'Ionic', level: 7 },
  { type: 'Package', name: 'Pandas', level: 7 },
  { type: 'Package', name: 'PyArrow', level: 7 },
  { type: 'Package', name: 'React', level: 7 },
  { type: 'Package', name: 'Xamarin', level: 3 },
  { type: 'Package', name: 'Vue', level: 4 },
  { type: 'Package', name: 'WPF', level: 6 },

  { type: 'Protocol', name: 'FTP', level: 5 },
  { type: 'Protocol', name: 'HTTP', level: 5 },
  { type: 'Protocol', name: 'LDAP', level: 4 },
  { type: 'Protocol', name: 'REST', level: 7 },
  { type: 'Protocol', name: 'SOAP', level: 6 },

  { type: 'Source control', name: 'Git', level: 7 },
  { type: 'Source control', name: 'TFS', level: 5 },
])

const cats = computed(() => [...new Set(DATA.value.map((x) => x.type))])

const skillSearch = ref<string>('')
const catFilter = ref<string>('')

const sortKey = ref<keyof (typeof DATA.value)[0]>('type')
const sortOrder = ref(1)

const sorted = computed(() => {
  const skill = skillSearch.value.toLocaleLowerCase()
  const cat = catFilter.value

  return [...DATA.value]
    .filter((value) => {
      const skillMatch = skill === '' || value.name.toLocaleLowerCase().indexOf(skill) >= 0
      const catFilter = cat === '' || value.type === cat
      return skillMatch && catFilter
    })
    .sort((a, b) => {
      if (!sortKey.value) {
        return 0
      }

      const key = sortKey.value as keyof typeof a
      const x = a[key]
      const y = b[key]

      const comparison =
        (typeof x === 'string' && typeof y === 'string'
          ? x.localeCompare(y)
          : x > y
            ? 1
            : x < y
              ? -1
              : 0) * sortOrder.value

      return comparison
    })
})

const sortBy = (key: typeof sortKey.value) => {
  if (sortKey.value === key) {
    sortOrder.value = -sortOrder.value
  } else {
    sortKey.value = key
    sortOrder.value = 1
  }
}

const headerClasses = (index: keyof (typeof DATA.value)[0]) => {
  if (index !== sortKey.value) {
    return []
  }
  return [
    'active-sort-key',
    sortOrder.value === 1 ? 'active-sort-ascending' : 'active-sort-descending',
  ]
}

const headerStyle = (index: keyof (typeof DATA.value)[0], data: (typeof DATA.value)[0]) => {
  if (index !== 'level') {
    return {}
  }
  return {
    '--level': data[index],
    '--circumference': 2 * Math.PI * 16,
    '--dash': (data[index] / 10) * 2 * Math.PI * 16,
  }
}
</script>

<template>
  <label class="float">
    <input type="text" v-model="skillSearch" placeholder=" " />
    <span>Search skills</span>
  </label>
  <label class="float" :class="{ 'has-value': catFilter !== '' }">
    <select v-model="catFilter">
      <option value=""></option>
      <template v-for="(cat, index) in cats" :key="index">
        <option :value="cat">{{ cat }}</option>
      </template>
    </select>
    <span>Category</span>
  </label>
  <table>
    <thead>
      <tr>
        <template v-for="(header, index) in HEADERS" :key="index">
          <th @click="sortBy(index)" :class="[...headerClasses(index), `header-${index}`]">
            {{ header }}
          </th>
        </template>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(data, index) in sorted" :key="index">
        <template v-for="(header, headerKey) in HEADERS" :key="`${index}-${headerKey}`">
          <td :class="[`table-data-${headerKey}`]" :style="headerStyle(headerKey, data)">
            <svg v-if="headerKey === 'level'" viewBox="0 0 36 36" class="level-circle">
              <circle cx="18" cy="18" r="16" class="level-circle-bg" />
              <circle cx="18" cy="18" r="16" class="level-circle-progress" />
            </svg>
            <span>{{ data[headerKey] }}</span>
          </td>
        </template>
      </tr>
    </tbody>
  </table>
</template>

<style scoped>
label.float {
  position: relative;
  display: block;
  width: calc(max(75%, 250px));
  margin: 0 auto;
  margin-bottom: 1em;
}

label.float input {
  width: calc(100% - 1.25em);
}

label.float select {
  width: 100%;
  border: 1px solid #0c637e;
}

label.float select option {
  color: #000;
}

label.float select option:hover,
label.float select option:checked {
  color: #000;
}

label.float input,
label.float select {
  background-color: transparent;
  color: #eff;
  padding: 1.5em 0.75em 0.5em 0.75em;
  border: none;
  border-bottom: 1px solid #0c637e;
  font-size: 1em;
}

label.float input:focus,
label.float select:focus {
  outline: none;
  border-bottom: 1px solid #5ecdf0;
}

label.float span {
  background-color: transparent;
  color: #0c637e;
  position: absolute;
  left: 0.75em;
  top: 50%;
  transform: translateY(-50%);
  transition: all 0.2s ease;
  pointer-events: none;
  padding: 0 0.25em;
}

label.float input:focus + span,
label.float input:not(:placeholder-shown) + span,
label.float select:focus + span,
label.float.has-value select + span {
  top: 0;
  font-size: 0.75em;
  transform: translateY(0);
  color: #5ecdf0;
}

table {
  width: 100%;
}

table thead {
  font-size: 1.1em;
  font-weight: bold;
  color: #5ecdf0;
}

th {
  text-align: left;
}

th.header-level {
  min-width: 5em;
}

th.active-sort-ascending::after {
  content: '⛛';
  display: inline-block;
  padding-left: 0.5em;
}
th.active-sort-descending::after {
  content: '⛛';
  display: inline-block;
  padding-right: 0.5em;
  transform: rotate(180deg);
}

td.table-data-level {
  position: relative;
  text-align: center;
}

.level-circle {
  width: 2.5em;
  height: 2.5em;
  transform: rotate(-90deg);
  display: block;
  margin: 0 auto;
}

.level-circle-bg {
  fill: none;
  stroke: #0c637e;
  stroke-width: 2;
}

.level-circle-progress {
  fill: none;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-dasharray: var(--dash) var(--circumference);
  stroke: hsl(calc(var(--level) * 12), 70%, 50%);
}

td.table-data-level span {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  color: #eff;
  pointer-events: none;
}
</style>
