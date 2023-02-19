import {useEffect, useRef, useState} from "react"
import {useRouter} from "next/router"
import {E, connect, updateState} from "/utils/state"
import "focus-visible/dist/focus-visible"
import {Center, Divider, HStack, Heading, Image, Link, Spacer, Text, VStack, useColorMode} from "@chakra-ui/react"
import NextLink from "next/link"
import NextHead from "next/head"

const EVENT = "ws://localhost:8000/event"
export default function Component() {
const [state, setState] = useState({"events": [{"name": "state.hydrate"}]})
const [result, setResult] = useState({"state": null, "events": [], "processing": false})
const router = useRouter()
const socket = useRef(null)
const { isReady } = router;
const { colorMode, toggleColorMode } = useColorMode()
const Event = events => setState({
  ...state,
  events: [...state.events, ...events],
})
useEffect(() => {
  if(!isReady) {
    return;
  }
  if (!socket.current) {
    connect(socket, state, setState, result, setResult, router, EVENT, ['websocket', 'polling'])
  }
  const update = async () => {
    if (result.state != null) {
      setState({
        ...result.state,
        events: [...state.events, ...result.events],
      })
      setResult({
        state: null,
        events: [],
        processing: false,
      })
    }
    await updateState(state, setState, result, setResult, router, socket.current)
  }
  update()
})
return (
<Center><VStack sx={{"width": "80%"}}><Heading sx={{"fontFamily": "Open Sans", "fontSize": "100px", "color": "#E8EAED"}}>{`Alec Jensen`}</Heading>
<Spacer sx={{"width": "20px"}}/>
<Divider sx={{"borderColor": "#3C4043"}}/>
<Spacer sx={{"width": "20px"}}/>
<Text sx={{"fontSize": "20px", "color": "#B6BABF"}}>{`Frontend Developer | Backend Developer | 3D Artist | Musician | Drone Pilot | `}
<NextLink href="https://cloud.alecj.tk/s/3fXAebqGMpAYyXe"
passHref={true}><Link isExternal={true}
sx={{"color": "#8AB4F8"}}>{`Photographer`}</Link></NextLink></Text>
<Spacer sx={{"width": "20px"}}/>
<Divider sx={{"borderColor": "#3C4043"}}/>
<Spacer sx={{"width": "20px"}}/>
<HStack sx={{"height": "70px", "width": "30%"}}><NextLink href="https://github.com/alec-jensen"
passHref={true}><Link isExternal={true}
sx={{"color": "#E8EAED"}}><Image src="/github-mark.svg"
sx={{"height": "60px"}}/></Link></NextLink>
<Spacer/>
<NextLink href="https://discord.gg/JjWEVXttFR"
passHref={true}><Link isExternal={true}
sx={{"color": "#E8EAED"}}><Image src="/discord.svg"
sx={{"height": "70px"}}/></Link></NextLink>
<Spacer/>
<NextLink href="https://www.youtube.com/@alecjensen"
passHref={true}><Link isExternal={true}
sx={{"color": "#E8EAED"}}><Image src="/youtube.svg"
sx={{"height": "70px"}}/></Link></NextLink></HStack>
<Spacer sx={{"width": "20px"}}/>
<Divider sx={{"borderColor": "#3C4043"}}/>
<Spacer sx={{"width": "20px"}}/>
<Text sx={{"textAlign": "center", "width": "50%", "fontSize": "20px", "color": "#B6BABF"}}>{`I'm a 15-year-old who is passionate about programming. I have a lot of experience creating frontends and backends using languages like Python, Java, and C++. When I'm not programming, I enjoy taking pictures, making videos, and playing the viola.`}</Text></VStack>
<NextHead><title>{`Alec Jensen`}</title>
<meta content="A Pynecone app."
name="description"/>
<meta content="favicon.ico"
property="og:image"/></NextHead></Center>
)
}