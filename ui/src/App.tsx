import React , { useEffect, useState } from 'react';
import PSLogo from "assets/PS_logo.svg";
import Plot from 'react-plotly.js';
import { Flex, Image, Text } from "@chakra-ui/react";
import { getRaceData } from  './actions';

import "@/App.css";

interface PlotType {
  name: string;
  x: number[];
  y: number[];
  type: string;
}

function App() {
  const [raceName, setRaceName] = useState<PlotType[] | undefined>();
  const [data, setData] = useState<PlotType[] | undefined>();

  const normaliseData = (data: any) => {
    const values = Object.keys(data).map((name: string, i: number)=> ({
      type: 'line',
      name,
      x: Object.keys(data[name]),
      y: Object.values(data[name]),
    }));

    setData(values);
  }

  useEffect(() => {
    const init = async () => {
      try {
        const response = await getRaceData();
        if (response.status === 200) {
          normaliseData(response.data[0].data);
          setRaceName(response.data[0].name);
        }
      } catch (err: unknown) {
        console.error(err);
      }
    }
    init();
  }, []);

  return (
    <Flex direction="column">
      <Image
        src={PSLogo}
        className="logo"
        alt="PurpleSector logo"
        minW={{ base: "650px" }}
      />
      <Text fontSize="5xl" fontWeight="medium">
        Coding Challenge - Lorenzo Campanis
      </Text>

      <Plot
        data={data}
        layout={{width: '100%', height: 500, title: `${raceName} Laps & Times`}}
      />
    </Flex>
  );
}

export default App;
