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
            '/scrapy':{
                target:'http://localhost:8090',
                // changeOrigin:true,
                pathRewrite:{
                    '^/scrapy':'/'
                }
            }
        }
    }
}