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
                target:'http://localhost:9080',
                // changeOrigin:true,
                pathRewrite:{
                    '^/scrapy':'/'
                }
            }
        }
    }
}