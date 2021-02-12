<template>
  <div id="app">  
   <Header /> 
   <AddTodo v-on:add-todo="addTodo"/> 
   <Todos v-bind:todos="todos" v-on:del-todo="deleteTodo" v-on:update-todo="updateStatus" />
  </div>
</template>

<script>
import Todos from './components/Todos';
import Header from './components/layout/header';
import AddTodo from './components/AddTodo';
import axios from 'axios'

export default {
  name: 'App',
  components: {
    Header,
    AddTodo,
    Todos
  },
  data() {
    return {
      todos: []
    }
  },
  methods: {
    deleteTodo(id) {
         axios.delete(`http://localhost:5000/todo/${id}`)
          .then(this.todos = this.todos.filter(todo => todo.id !== id))
          .catch(err => console.log(err));

    },
    addTodo(newTodo) {
        const {title, completed} = newTodo;

        axios.post('http://localhost:5000/todo/post/', {
          title,
          completed
        })
          .then(res => this.todos = [...this.todos, res.data])
          .catch(err => console.log(err));
     
    },
    updateStatus(id, completed){
      let title = "";
      
      axios.put(`http://localhost:5000/todo/update/${id}`, {
        id,
        title,
        completed
      })               
        .catch(err => console.log(err));

    }
  },
  created(){
    axios.get('http://localhost:5000/todos/')
    .then(res => this.todos = res.data)
    .then(res => console.log(res.data))
    .catch(err => console.log(err));
  }
}
</script>

<style>
* {
 box-sizing: border-box;
 margin: 0;
 padding: 0;
}

body {
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.4;
}

.btn {
  display: inline-block;
  border: none;
  background: #555;
  color: #fff;
  padding: 7px 20px;
  cursor: pointer;
}

.btn:hover {
  background: #666;
}

</style>
