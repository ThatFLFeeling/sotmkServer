const express = require('express')
const fs = require('fs')

const path = './time.txt'
const port = 80
const app = express()
//192.168.4.39
//stormy22


app.get('/lastscan', (req, res) => {
    try {
        if (fs.existsSync(path)) {
            res.json({
                message: "Last Scan time:",
                time: parseInt(fs.readFileSync(path, 'utf8'))
            })
        } else {
            res.json({
                message: "No file found",
                time: 0
            })
        }
      } catch(err) {
        console.error(err)
      }
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})
