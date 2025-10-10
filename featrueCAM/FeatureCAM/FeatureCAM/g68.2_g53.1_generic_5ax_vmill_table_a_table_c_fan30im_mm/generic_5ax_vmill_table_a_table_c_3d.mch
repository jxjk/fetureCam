<?xml version="1.0"?>
<VcMachine Version="9.0" Unit="millimeter">
  <Information>
    <InfoUserName>Administrator</InfoUserName>
    <InfoDateTime>Wed Apr  1 22:46:45 2020</InfoDateTime>
    <InfoVericutVersion>9.0.1</InfoVericutVersion>
    <InfoBuildDate>March 02, 2020 </InfoBuildDate>
    <InfoLibraryDate>03/02/20</InfoLibraryDate>
    <InfoCustomerName>LND-7330757468@CS</InfoCustomerName>
    <InfoCustomerID>094671</InfoCustomerID>
    <InfoServerID>001</InfoServerID>
    <InfoHostID>e4a7260eac6f</InfoHostID>
  </Information>
  <PriorityType>single</PriorityType>
  <MachineInitFile File="generic_5ax_vmill_table_a_table_c_3d.ini" />
  <Table Name="Initial Machine Location">
    <Row Index="1" SubIndex="1" Auto="manual">
      <System>1</System>
      <Value>0</Value>
      <Value>0</Value>
      <Value>0</Value>
    </Row>
  </Table>
  <Collision>
    <Between Sub1="on" Sub2="on" Tol="0">
      <Component>X</Component>
      <Component>Base_A</Component>
    </Between>
  </Collision>
  <Component Name="Base"
   Subsystem="1"
   Type="base" Visible="machine" Draw="shaded" XRGB="0x00FFFFFF">
    <Attach></Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00FFFFFF"/>
  </Component>
  <Component Name="X"
   Subsystem="1"
   Type="linear" Visible="machine" Draw="shaded" XRGB="0x00969696">
    <Attach>Base</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00969696"/>
    <Link Axis="X" PartSide="auto" Register="X"
     RapidRate="5000" Accel="125" Decel="125" MaxLinearVelocity="5000" MaxCornerVelocity="600">
      <AxisPriority PriorityGroup="0" PriorityPos="1" InterpolatedPos="on" PriorityNeg="1" InterpolatedNeg="on"/>
      <TlRecord TlGroup="0" TlComp="X" TlMin="0" TlMax="0" TlCompCond="" TlMinCond="0" TlMaxCond="0" TlIgnore="on"/>
    </Link>
  </Component>
  <Component Name="Y"
   Subsystem="1"
   Type="linear" Visible="machine" Draw="shaded" XRGB="0x00969696">
    <Attach>X</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00969696"/>
    <Link Axis="Y" PartSide="auto" Register="Y"
     RapidRate="5000" Accel="125" Decel="125" MaxLinearVelocity="5000" MaxCornerVelocity="600">
      <AxisPriority PriorityGroup="0" PriorityPos="1" InterpolatedPos="on" PriorityNeg="1" InterpolatedNeg="on"/>
      <TlRecord TlGroup="0" TlComp="Y" TlMin="0" TlMax="0" TlCompCond="" TlMinCond="0" TlMaxCond="0" TlIgnore="on"/>
    </Link>
    <Block Length="260" Width="1100" Height="400" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="-130" Y="250" Z="400"/>
      </ModelMatrix>
    </Block>
  </Component>
  <Component Name="Z"
   Subsystem="1"
   Type="linear" Visible="machine" Draw="shaded" XRGB="0x00969696">
    <Attach>Y</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00969696"/>
    <Link Axis="Z" PartSide="auto" Register="Z"
     RapidRate="5000" Accel="125" Decel="125" MaxLinearVelocity="5000" MaxCornerVelocity="600">
      <AxisPriority PriorityGroup="0" PriorityPos="1" InterpolatedPos="on" PriorityNeg="1" InterpolatedNeg="on"/>
      <TlRecord TlGroup="0" TlComp="Z" TlMin="0" TlMax="0" TlCompCond="" TlMinCond="0" TlMaxCond="0" TlIgnore="on"/>
    </Link>
    <Block Length="50" Width="50" Height="1000" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="100" Y="150" Z="100"/>
      </ModelMatrix>
    </Block>
    <Block Length="50" Width="50" Height="1000" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="-150" Y="150" Z="100"/>
      </ModelMatrix>
    </Block>
    <Block Length="300" Width="50" Height="1000" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="-1" Y="1.22464679915e-16" Z="0"/>
        <MatrixYAxis X="-1.22464679915e-16" Y="-1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="150" Y="250" Z="100"/>
      </ModelMatrix>
    </Block>
    <Cylinder Radius="150" Height="600" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="0" Y="0" Z="100"/>
      </ModelMatrix>
    </Cylinder>
    <Block Length="300" Width="150" Height="600" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="-150" Y="0" Z="100"/>
      </ModelMatrix>
    </Block>
  </Component>
  <Component Name="W"
   Subsystem="1"
   Type="linear" Visible="machine" Draw="shaded" XRGB="0x000000C8">
    <Attach>Z</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x000000C8"/>
    <Link Axis="Z" PartSide="auto" Register="W"
     RapidRate="5000" Accel="125" Decel="125" MaxLinearVelocity="5000" MaxCornerVelocity="600">
      <AxisPriority PriorityGroup="0" PriorityPos="1" InterpolatedPos="on" PriorityNeg="1" InterpolatedNeg="on"/>
    </Link>
    <Cylinder Radius="60" Height="300" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="0" Y="0" Z="100"/>
      </ModelMatrix>
    </Cylinder>
  </Component>
  <Component Name="Spindle"
   Subsystem="1"
   Type="spindle" Visible="machine" Draw="shaded" XRGB="0x00C8C8C8">
    <Attach>W</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00C8C8C8"/>
    <Link Axis="Z" PartSide="auto" Register="Spindle">
    </Link>
    <Cylinder Radius="40" Height="40" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="0" Y="0" Z="0"/>
      </ModelMatrix>
    </Cylinder>
    <Cylinder Radius="60" Height="60" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="0" Y="0" Z="40"/>
      </ModelMatrix>
    </Cylinder>
  </Component>
  <Component Name="U"
   Subsystem="1"
   Type="linear" Visible="machine" Draw="shaded" XRGB="0x00FF0000">
    <Attach>Spindle</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00FF0000"/>
    <Link Axis="X" PartSide="auto" Register="U"
     RapidRate="5000" Accel="125" Decel="125" MaxLinearVelocity="5000" MaxCornerVelocity="600">
      <AxisPriority PriorityGroup="0" PriorityPos="1" InterpolatedPos="on" PriorityNeg="1" InterpolatedNeg="on"/>
    </Link>
  </Component>
  <Component Name="Tool"
   Subsystem="1"
   Type="tool" Visible="all" Draw="translucent" XRGB="0x00C8C8C8">
    <Attach>U</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00C8C8C8"/>
    <Tool TurretIndex="1"/>
    <Link Axis="Z" PartSide="auto" Register="Tool">
    </Link>
  </Component>
  <Component Name="Light_OFF"
   Subsystem="1"
   Type="other" Visible="machine" Draw="shaded" XRGB="0x00690000">
    <Attach>W</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00690000"/>
    <Cylinder Radius="5" Height="1" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="-1.124819837e-32" Y="6.12323399574e-17" Z="1"/>
        <MatrixYAxis X="-2.4492935983e-16" Y="1" Z="-6.12323399574e-17"/>
        <MatrixZAxis X="-1" Y="-2.4492935983e-16" Z="3.74939945666e-33"/>
        <MatrixOrigin X="40" Y="7.34788079488e-15" Z="10"/>
      </ModelMatrix>
    </Cylinder>
    <Cylinder Radius="5" Height="1" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="-6.12323399574e-17" Y="-7.49879891331e-33" Z="1"/>
        <MatrixYAxis X="-1" Y="-1.83697019872e-16" Z="-6.12323399574e-17"/>
        <MatrixZAxis X="1.83697019872e-16" Y="-1" Z="3.74939945666e-33"/>
        <MatrixOrigin X="-4.89858719659e-15" Y="40" Z="10"/>
      </ModelMatrix>
    </Cylinder>
    <Cylinder Radius="5" Height="1" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="3.74939945666e-33" Y="-6.12323399574e-17" Z="1"/>
        <MatrixYAxis X="1.22464679915e-16" Y="-1" Z="-6.12323399574e-17"/>
        <MatrixZAxis X="1" Y="1.22464679915e-16" Z="3.74939945666e-33"/>
        <MatrixOrigin X="-40" Y="-2.44929359829e-15" Z="10"/>
      </ModelMatrix>
    </Cylinder>
    <Cylinder Radius="5" Height="1" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="6.12323399574e-17" Y="1.38875278004e-45" Z="1"/>
        <MatrixYAxis X="1" Y="6.12323399574e-17" Z="-6.12323399574e-17"/>
        <MatrixZAxis X="-6.12323399574e-17" Y="1" Z="3.74939945666e-33"/>
        <MatrixOrigin X="7.88860905221e-31" Y="-40" Z="10"/>
      </ModelMatrix>
    </Cylinder>
  </Component>
  <Component Name="Light_On_KO"
   Subsystem="1"
   Type="other" Visible="none" Draw="shaded" XRGB="0x00FF0000">
    <Attach>W</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00FF0000"/>
    <Cylinder Radius="5" Height="1" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="-1.124819837e-32" Y="6.12323399574e-17" Z="1"/>
        <MatrixYAxis X="-2.4492935983e-16" Y="1" Z="-6.12323399574e-17"/>
        <MatrixZAxis X="-1" Y="-2.4492935983e-16" Z="3.74939945666e-33"/>
        <MatrixOrigin X="40" Y="7.34788079488e-15" Z="10"/>
      </ModelMatrix>
    </Cylinder>
    <Cylinder Radius="5" Height="1" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="-6.12323399574e-17" Y="-7.49879891331e-33" Z="1"/>
        <MatrixYAxis X="-1" Y="-1.83697019872e-16" Z="-6.12323399574e-17"/>
        <MatrixZAxis X="1.83697019872e-16" Y="-1" Z="3.74939945666e-33"/>
        <MatrixOrigin X="-4.89858719659e-15" Y="40" Z="10"/>
      </ModelMatrix>
    </Cylinder>
    <Cylinder Radius="5" Height="1" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="3.74939945666e-33" Y="-6.12323399574e-17" Z="1"/>
        <MatrixYAxis X="1.22464679915e-16" Y="-1" Z="-6.12323399574e-17"/>
        <MatrixZAxis X="1" Y="1.22464679915e-16" Z="3.74939945666e-33"/>
        <MatrixOrigin X="-40" Y="-2.44929359829e-15" Z="10"/>
      </ModelMatrix>
    </Cylinder>
    <Cylinder Radius="5" Height="1" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="6.12323399574e-17" Y="1.38875278004e-45" Z="1"/>
        <MatrixYAxis X="1" Y="6.12323399574e-17" Z="-6.12323399574e-17"/>
        <MatrixZAxis X="-6.12323399574e-17" Y="1" Z="3.74939945666e-33"/>
        <MatrixOrigin X="7.88860905221e-31" Y="-40" Z="10"/>
      </ModelMatrix>
    </Cylinder>
  </Component>
  <Component Name="Light_On_OK"
   Subsystem="1"
   Type="other" Visible="none" Draw="shaded" XRGB="0x00FFFF00">
    <Attach>W</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00FFFF00"/>
    <Cylinder Radius="5" Height="1" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="-1.124819837e-32" Y="6.12323399574e-17" Z="1"/>
        <MatrixYAxis X="-2.4492935983e-16" Y="1" Z="-6.12323399574e-17"/>
        <MatrixZAxis X="-1" Y="-2.4492935983e-16" Z="3.74939945666e-33"/>
        <MatrixOrigin X="40" Y="7.34788079488e-15" Z="10"/>
      </ModelMatrix>
    </Cylinder>
    <Cylinder Radius="5" Height="1" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="-6.12323399574e-17" Y="-7.49879891331e-33" Z="1"/>
        <MatrixYAxis X="-1" Y="-1.83697019872e-16" Z="-6.12323399574e-17"/>
        <MatrixZAxis X="1.83697019872e-16" Y="-1" Z="3.74939945666e-33"/>
        <MatrixOrigin X="-4.89858719659e-15" Y="40" Z="10"/>
      </ModelMatrix>
    </Cylinder>
    <Cylinder Radius="5" Height="1" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="3.74939945666e-33" Y="-6.12323399574e-17" Z="1"/>
        <MatrixYAxis X="1.22464679915e-16" Y="-1" Z="-6.12323399574e-17"/>
        <MatrixZAxis X="1" Y="1.22464679915e-16" Z="3.74939945666e-33"/>
        <MatrixOrigin X="-40" Y="-2.44929359829e-15" Z="10"/>
      </ModelMatrix>
    </Cylinder>
    <Cylinder Radius="5" Height="1" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="6.12323399574e-17" Y="1.38875278004e-45" Z="1"/>
        <MatrixYAxis X="1" Y="6.12323399574e-17" Z="-6.12323399574e-17"/>
        <MatrixZAxis X="-6.12323399574e-17" Y="1" Z="3.74939945666e-33"/>
        <MatrixOrigin X="7.88860905221e-31" Y="-40" Z="10"/>
      </ModelMatrix>
    </Cylinder>
  </Component>
  <Component Name="Base_A"
   Subsystem="1"
   Type="other" Visible="machine" Draw="shaded" XRGB="0x00FFFFFF">
    <Attach>Base</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00FFFFFF"/>
    <STL Unit="millimeter" Normal="outward" Visible="on" XRGB="0x80000000">
      <File>generic_5ax_vmill_table_a_table_c_3d_base.stl</File>
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="-1250" Y="1300" Z="-1400"/>
      </ModelMatrix>
    </STL>
    <STL Unit="millimeter" Normal="outward" Visible="on" XRGB="0x80000000">
      <File>generic_5ax_vmill_table_a_table_c_3d_a_motors.stl</File>
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="6.12323399574e-17" Y="1" Z="0"/>
        <MatrixYAxis X="-1" Y="6.12323399574e-17" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="-1250" Y="-1252" Z="-1400"/>
      </ModelMatrix>
    </STL>
  </Component>
  <Component Name="A"
   Subsystem="1"
   Type="rotary" Visible="machine" Draw="shaded" XRGB="0x00969696" RotarySpin="off">
    <Attach>Base_A</Attach>
    <Position X="0" Y="0" Z="-500"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00969696"/>
    <Link Axis="X" PartSide="auto" Register="A"
     RapidRate="5000" Accel="125" Decel="125" MaxLinearVelocity="5000" MaxCornerVelocity="600">
      <AxisPriority PriorityGroup="0" PriorityPos="1" InterpolatedPos="on" PriorityNeg="1" InterpolatedNeg="on"/>
      <TlRecord TlGroup="0" TlComp="A" TlMin="0" TlMax="0" TlCompCond="" TlMinCond="0" TlMaxCond="0" TlIgnore="on"/>
    </Link>
    <Block Length="1000" Width="300" Height="170" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="-500" Y="-150" Z="-200"/>
      </ModelMatrix>
    </Block>
    <Cylinder Radius="250" Height="200" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="0" Y="0" Z="-200"/>
      </ModelMatrix>
    </Cylinder>
    <Cylinder Radius="150" Height="75" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="6.12323399574e-17" Y="0" Z="-1"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="1" Y="0" Z="6.12323399574e-17"/>
        <MatrixOrigin X="425" Y="0" Z="0"/>
      </ModelMatrix>
    </Cylinder>
    <Cylinder Radius="150" Height="75" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="6.12323399574e-17" Y="0" Z="-1"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="1" Y="0" Z="6.12323399574e-17"/>
        <MatrixOrigin X="-500" Y="0" Z="0"/>
      </ModelMatrix>
    </Cylinder>
    <Cylinder Radius="225" Height="125" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="6.12323399574e-17" Y="0" Z="-1"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="1" Y="0" Z="6.12323399574e-17"/>
        <MatrixOrigin X="-625" Y="0" Z="0"/>
      </ModelMatrix>
    </Cylinder>
    <Cylinder Radius="225" Height="125" Visible="on" XRGB="0x80000000">
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="6.12323399574e-17" Y="0" Z="-1"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="1" Y="0" Z="6.12323399574e-17"/>
        <MatrixOrigin X="500" Y="0" Z="0"/>
      </ModelMatrix>
    </Cylinder>
  </Component>
  <Component Name="C"
   Subsystem="1"
   Type="rotary" Visible="machine" Draw="shaded" XRGB="0x004B4B4B" RotarySpin="off">
    <Attach>A</Attach>
    <Position X="0" Y="0" Z="50"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x004B4B4B"/>
    <Link Axis="Z" PartSide="auto" Register="C"
     RapidRate="5000" Accel="125" Decel="125" MaxLinearVelocity="5000" MaxCornerVelocity="600">
      <AxisPriority PriorityGroup="0" PriorityPos="1" InterpolatedPos="on" PriorityNeg="1" InterpolatedNeg="on"/>
      <TlRecord TlGroup="0" TlComp="C" TlMin="0" TlMax="0" TlCompCond="" TlMinCond="0" TlMaxCond="0" TlIgnore="on"/>
    </Link>
    <STL Unit="millimeter" Normal="outward" Visible="on" XRGB="0x80000000">
      <File>generic_5ax_vmill_table_a_table_c_3d_c.stl</File>
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="0" Y="0" Z="0"/>
      </ModelMatrix>
    </STL>
  </Component>
  <Component Name="Attach"
   Subsystem="1"
   Type="attach" Visible="machine" Draw="shaded" XRGB="0x00FF0000">
    <Attach>C</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00FF0000"/>
  </Component>
  <Component Name="Enclosure"
   Subsystem="1"
   Type="other" Visible="none" Draw="translucent" XRGB="0x00FFFFFF">
    <Attach>Base</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00FFFFFF"/>
    <STL Unit="millimeter" Normal="outward" Visible="on" XRGB="0x80000000">
      <File>generic_5ax_vmill_table_a_table_c_3d_enclosure.stl</File>
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="-1250" Y="1300" Z="-1400"/>
      </ModelMatrix>
    </STL>
  </Component>
  <Component Name="Door"
   Subsystem="Door"
   Type="linear" Visible="none" Draw="translucent" XRGB="0x00FFFFFF">
    <Attach>Enclosure</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x00FFFFFF"/>
    <Link Axis="Z" PartSide="auto" Register="Z"
     RapidRate="5000" Accel="125" Decel="125" MaxLinearVelocity="5000" MaxCornerVelocity="600">
      <AxisPriority PriorityGroup="0" PriorityPos="1" InterpolatedPos="on" PriorityNeg="1" InterpolatedNeg="on"/>
      <TlRecord TlGroup="0" TlComp="Door" TlMin="0" TlMax="0" TlCompCond="" TlMinCond="0" TlMaxCond="0" TlIgnore="on"/>
    </Link>
    <STL Unit="millimeter" Normal="outward" Visible="on" XRGB="0x80000000">
      <File>generic_5ax_vmill_table_a_table_c_3d_door.stl</File>
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="1" Z="0"/>
        <MatrixZAxis X="0" Y="0" Z="1"/>
        <MatrixOrigin X="-1250" Y="1300" Z="-1400"/>
      </ModelMatrix>
    </STL>
  </Component>
  <Component Name="Logo"
   Subsystem="1"
   Type="other" Visible="none" Draw="shaded" XRGB="0x000000C8">
    <Attach>Enclosure</Attach>
    <Position X="0" Y="0" Z="0"/>
    <Rotation I="0" J="0" K="0"/>
    <Appearance Name="Steel" Ambient="0.3" Diffuse="0.8" Reflect="0.2" Specular="0.5" Shininess="64" Translucency="1" XRGB="0x000000C8"/>
    <STL Unit="millimeter" Normal="outward" Visible="on" XRGB="0x80000000">
      <File>cgtech_vericut_logo.stl</File>
      <EdgeAngle>30</EdgeAngle>
      <ModelMatrix>
        <MatrixXAxis X="1" Y="0" Z="0"/>
        <MatrixYAxis X="0" Y="6.12323399574e-17" Z="1"/>
        <MatrixZAxis X="0" Y="-1" Z="6.12323399574e-17"/>
        <MatrixOrigin X="-1040.4933" Y="-1230" Z="677.233"/>
      </ModelMatrix>
    </STL>
  </Component>
  <Preview Image="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"/>
</VcMachine>
