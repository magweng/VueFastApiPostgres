<template>
    <div>
        <form @submit="addTodo">
            <input type="text" v-model="title" name="title" placeholder="Add todo...">
            <input type="submit" value="Submit" class="btn">
        </form>
    </div>
</template>

<script>

export default {
    name: "AddTodo",
    data() {
        return {
            title: ''
        }
     },
     methods: {
         addTodo(e) {
             e.preventDefault();
             const newTodo = {
                 title: this.title, //v-model="title"
                 completed: false
             }
             //Send up to parrent
             this.$emit('add-todo', newTodo);
             this.title = "";
         }
     }
}
</script>

<style scoped>
    form {
        display: flex;
    }

    input[type="text"] {
        flex: 10;
        padding: 5px; 
    }

    input[type="submit"] {
        flex: 2;        
    }

</style>