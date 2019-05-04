module.exports={
    devServer:{
        proxy:{
            '/flask':{
                target:'http://localhost:5000',
                changeOrigin: true,
                pathRewrite:{
                    '^/flask':'/'
                }
            },
            '/scrapyrt':{
                target:'http://localhost:9080/crawl.json',
                // changeOrigin:true,
                pathRewrite:{
                    '^/scrapyrt':'/'
                }
            }
        }
    }
}