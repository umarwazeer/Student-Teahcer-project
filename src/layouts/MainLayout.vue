<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />
      </q-toolbar>
    </q-header>

    <q-drawer
      class="bg-grey-9 text-white"
      @mouseover="miniState = false"
      @mouseout="miniState = true"
      :breakpoint="500"
      bordered
      :width="200"
      v-model="leftDrawerOpen"
    >
      <q-list padding class="q-pt-md">
        <!----------------------Add Employee-------------->
    
            <q-expansion-item
          expand-separator
          dense
          icon="time_to_leave"
          label="Student"
          
        >
          <q-item clickable v-ripple active to="/StudentList" class="text-white">
            <q-item-section avatar class="">
              <q-icon name="group" />
            </q-item-section>
            <q-item-section>
              <q-item-label>Add Student</q-item-label>
            </q-item-section>
          </q-item>
           <q-item clickable v-ripple active to="" class="text-white">
            <q-item-section avatar class="">
              <q-icon name="list" />
            </q-item-section>
            <q-item-section>
              <q-item-label>Student List</q-item-label>
            </q-item-section>
          </q-item>
        </q-expansion-item>

        <!---------------------Employee Profile------------------->
        <q-item clickable active to="" class="text-white">
          <q-item-section avatar class="">
            <q-icon name="addprofile" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Teacher</q-item-label>
          </q-item-section>
        </q-item>
        <!---------------------Create Profile------------------->
     
        <!-- </q-list> -->

        <!-- <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        /> -->
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'

const linksList = [
  {
    title: 'Docs',
    caption: 'quasar.dev',
    icon: 'school',
    link: 'https://quasar.dev'
  },
  {
    title: 'Employee List',
    caption: 'Add and list of employee',
    icon: 'code',
    link: '/employeeList'
  },
]

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink
  },

  setup () {
    const leftDrawerOpen = ref(false)

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
})
</script>
