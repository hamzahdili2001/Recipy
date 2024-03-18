<template>
    <div style="height: 600px; background-color: #FDBF60;"
        class="d-flex mb-15 justify-center align-center text-center text-white">
        <div class="sub-container">
            <h1 class="mb-3">Deliciousness to your inbox</h1>
            <p class="mb-3 w-50 mx-auto">Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi obcaecati cum
                hic ab
                corporis. Aut odio
                maiores harum a molestias voluptate.</p>
            <div class="mt-10">
                <input type="text" placeholder="EMAIL" class="pa-3 sub-input">
                <button class="pa-3 sub-btn">JOIN</button>
            </div>
        </div>
    </div>
</template>


<style>
.sub-container h1 {
    font-size: 3em;
}

.sub-container p {
    font-size: .90rem;
    color: aliceblue
}

.sub-input {
    border: none;
    outline: none;
    background-color: aliceblue;
    border-radius: 2px 0 0 2px;
    width: 400px;
}

.sub-btn {
    background-color: #FF8911;
    border: none;
    width: 100px;
    border-radius: 0 2px 2px 0;
    text-transform: uppercase;
    font-weight: 500;
}
</style>