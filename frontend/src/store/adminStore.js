import { reactive } from "vue";

// path:
//  category = 1
//  manager_approvals = 2

// dialogueType:
//   add = 1
//   edit = 2
//   delete = 2

const adminStore = reactive({
  path: 1,
  dialogueType: 1,
  catName: '',
  catDesc: ''
})

export {adminStore}