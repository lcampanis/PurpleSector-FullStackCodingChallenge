import PSLogo from "assets/PS_logo.svg";
import "@/App.css";
import { Flex, Image, Text } from "@chakra-ui/react";

function App() {
  return (
    <Flex direction="column">
      <Image
        src={PSLogo}
        className="logo"
        alt="PurpleSector logo"
        minW={{ base: "650px" }}
      />
      <Text fontSize="5xl" fontWeight="medium">
        Coding Challenge - Add your name here before the interview
      </Text>
    </Flex>
  );
}

export default App;
