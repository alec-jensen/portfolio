import {Head, Html, Main, NextScript} from "next/document"
import {ColorModeScript} from "@chakra-ui/react"
export default function Document() {
return (
<Html><Head><link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@600&display=swap"
rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
rel="stylesheet"/></Head>
<body><ColorModeScript initialColorMode="light"/>
<Main/>
<NextScript/></body></Html>
)
}