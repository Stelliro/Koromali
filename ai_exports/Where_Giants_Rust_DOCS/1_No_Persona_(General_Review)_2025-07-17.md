# AI Task: No Persona (General Review)
## Timestamp: 2025-07-17T21:30:58.727065

---SYSTEM-PROMPT---

You are a helpful and experienced software developer. Your goal is to perform a general code review based on the user's instructions and the provided files. Offer concrete suggestions for improvement.

---USER-PROMPT---

# Project Review Request

**User's Goal:**
Perform a general review of the provided code.

---
**Project File Tree:**
```
/Where_Giants_Rust_DOCS
 └── 01_ENGINE_DESIGN
     ├── 01_Engine_Overview_and_Philosophy.md
     ├── 02_ENGINE_MODULES
     │   ├── 01_Core_Loop_and_State_Manager.md
     │   ├── 02_Platform_and_Windowing.md
     │   ├── 03_Input_Handler.md
     │   ├── 04_2D_Renderer.md
     │   ├── 05_3D_Renderer.md
     │   ├── 06_Physics_Engine.md
     │   ├── 07_Audio_Engine.md
     │   ├── 08_UI_System.md
     │   └── 09_Asset_Pipeline.md
     └── 03_Engine_API_Reference.md

```
---
**Files for Review:**
### File: `/01_ENGINE_DESIGN/03_Engine_API_Reference.md`
```md
# Engine API Reference: Stelliferrum Forge v0.1

## **1.0. Core Purpose & Naming Conventions**
This document is the master Application Programming Interface (API) Reference. It defines the public functions exposed by each core engine module. All inter-module communication **must** adhere to this contract.

*   **Naming Convention:** Functions will be referenced by `ModuleName.FunctionName()`. For example, `Renderer.DrawSprite()`.
*   **Data Types:** Standard types like `int`, `float`, `string`, `bool` will be used.
    *   `Vector2`: An object containing `{x, y}` coordinates.
    *   `Vector3`: An object containing `{x, y, z}` coordinates.
    *   `Color`: An object containing `{r, g, b, a}` values (0-255).
    *   `EntityID`: A unique integer identifier for a game object.
    *   `AssetID`: A unique string identifier for a loaded asset (e.g., `"sprites/player.png"`).

---
## **2.0. The Core Engine API**

*   **Function:** `Engine.Shutdown()`
    *   **Description:** Initiates the engine shutdown sequence, saving any required data and closing the application.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function:** `Engine.GetDeltaTime()`
    *   **Description:** Returns the time, in seconds, that has passed since the last frame. Essential for creating frame-rate indexpendent movement and physics.
    *   **Parameters:** None.
    *   **Returns:** `float`.

---
## **3.0. Platform Module API**
*(Manages the OS-level window)*

*   **Function:** `Platform.GetWindowSize()`
    *   **Description:** Returns the current dimensions of the game window.
    *   **Parameters:** None.
    *   **Returns:** `Vector2` `{width, height}`.

---
## **4.0. Input Module API**
*(Manages all player input)*

*   **Function:** `Input.IsKeyDown(keyCode)`
    *   **Description:** Checks if a specific keyboard key is currently being held down.
    *   **Parameters:** `keyCode` (string, e.g., `"W"`, `"Space"`).
    *   **Returns:** `bool`.

*   **Function:** `Input.IsKeyPressed(keyCode)`
    *   **Description:** Checks if a specific keyboard key was just pressed down on *this frame only*. Essential for single-press actions like jumping or interacting.
    *   **Parameters:** `keyCode` (string).
    *   **Returns:** `bool`.

*   **Function:** `Input.IsMouseButtonDown(buttonCode)`
    *   **Description:** Checks if a mouse button is currently held down.
    *   **Parameters:** `buttonCode` (int, `0`=Left, `1`=Right, `2`=Middle).
    *   **Returns:** `bool`.

*   **Function:** `Input.GetMousePosition()`
    *   **Description:** Returns the current (X, Y) pixel coordinates of the mouse cursor relative to the window.
    *   **Parameters:** None.
    *   **Returns:** `Vector2`.

---
## **5.0. Renderer Module API**
*(Manages all drawing to the screen)*

*   **Function:** `Renderer.BeginFrame()`
    *   **Description:** Prepares the renderer for a new frame. Should be called once at the start of the rendering phase. Clears the screen to a default color.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function:** `Renderer.EndFrame()`
    *   **Description:** Finishes the rendering process and displays the completed frame on the screen.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function:** `Renderer.DrawSprite(assetID, position, scale, rotation, color)`
    *   **Description:** Draws a 2D sprite to the screen.
    *   **Parameters:**
        *   `assetID` (AssetID): The unique identifier for the loaded image asset.
        *   `position` (Vector2): The world-space coordinate to draw the sprite's center.
        *   `scale` (Vector2, optional, default=`{1,1}`): The horizontal/vertical scale.
        *   `rotation` (float, optional, default=`0`): Rotation in degrees.
        *   `color` (Color, optional, default=`white`): A color tint to apply to the sprite.
    *   **Returns:** `void`.

*   **Function:** `Renderer.DrawText(text, position, fontID, size, color)`
    *   **Description:** Renders text to the screen. For UI elements.
    *   **Parameters:**
        *   `text` (string): The text to be displayed.
        *   `position` (Vector2): The screen-space pixel coordinate for the text's top-left corner.
        *   `fontID` (AssetID): The identifier for the loaded font asset.
        *   `size` (int): The font size.
        *   `color` (Color): The color of the text.
    *   **Returns:** `void`.

*   **Function:** `Renderer.SetCameraPosition(position)`
    *   **Description:** Sets the world-space position that the camera should be centered on.
    *   **Parameters:** `position` (Vector2).
    *   **Returns:** `void`.

---
## **6.0. Asset Manager API**
*(Manages loading/unloading of all game assets)*

*   **Function:** `Assets.LoadTexture(filePath)`
    *   **Description:** Loads an image file from disk into memory and assigns it a unique ID. If already loaded, it just returns the existing ID.
    *   **Parameters:** `filePath` (string, e.g., `"sprites/player.png"`).
    *   **Returns:** `AssetID` (which is often just the file path string itself).

*   **Function:** `Assets.LoadSound(filePath)`
    *   **Description:** Loads a sound file from disk into memory.
    *   **Parameters:** `filePath` (string, e.g., `"sfx/footstep.wav"`).
    *   **Returns:** `AssetID`.

---
## **7.0. Audio Module API**
*(Manages playing sounds and music)*

*   **Function:** `Audio.PlaySound(assetID, volume)`
    *   **Description:** Plays a loaded sound effect once.
    *   **Parameters:**
        *   `assetID` (AssetID): The identifier of the sound to play.
        *   `volume` (float, optional, default=`1.0`): The volume from 0.0 to 1.0.
    *   **Returns:** `void`.

*   **Function:** `Audio.PlayMusic(assetID, volume, loop)`
    *   **Description:** Plays a music track. Fades out any currently playing music.
    *   **Parameters:**
        *   `assetID` (AssetID).
        *   `volume` (float, optional, default=`1.0`).
        *   `loop` (bool, optional, default=`true`).
    *   **Returns:** `void`.

---
## **8.0. Physics Module API**
*(Manages all physical interactions)*

*   **Function:** `Physics.CreateBody(entityID, position, shape, type)`
    *   **Description:** Adds a physical body for an entity to the physics simulation.
    *   **Parameters:**
        *   `entityID` (EntityID): The entity to associate this body with.
        *   `position` (Vector2): The initial world position.
        *   `shape` (object, e.g., `{type:'circle', radius:16}` or `{type:'box', width:32, height:32}`): The collision shape.
        *   `type` (string, e.g., `"static"`, `"dynamic"`): Static bodies don't move; dynamic bodies are affected by forces.
    *   **Returns:** `bool` (success).

*   **Function:** `Physics.ApplyForce(entityID, forceVector)`
    *   **Description:** Applies a directional force to a dynamic body. The primary way game logic interacts with physics.
    *   **Parameters:** `entityID` (EntityID), `forceVector` (Vector2).
    *   **Returns:** `void`.

*   **Function:** `Physics.GetPosition(entityID)`
    *   **Description:** Gets the current position of an entity as determined by the physics simulation. The renderer will use this to know where to draw the entity.
    *   **Parameters:** `entityID` (EntityID).
    *   **Returns:** `Vector2`.
```

### File: `/01_ENGINE_DESIGN/01_Engine_Overview_and_Philosophy.md`
```md
# Engine Overview & Philosophy: The Stelliferrum Forge

## **1.0. Core Mission Statement**

This document outlines the guiding principles for the development of the **Stelliferrum Forge**. Our mission is to forge a **lightweight, custom-built, and highly specialized** game engine. It will not compete with generic engines. Instead, it is being architected from the ground up to serve one unifying, foundational principle:

**The Principle of Physicality: Everything Has Weight.**

Every object, action, and even phenomenon in our world is governed by a simulated **mass and material density**. From the heft of a greatsword, to the structural integrity of a fortress, to the very propagation of sound itself—everything is a calculation of weight, impact, and material response. This principle dictates all other design pillars.

## **2.0. The Five Pillars of Development**

#### **2.1. Pillar 1: Simulated Mass & Materiality (The Foundation)**
*   **The What:** Every entity in the world has a defined `mass` and `material_type`. A wooden arrow has less mass than a steel bolt. A stone wall is denser than a wooden one.
*   **The Why:** This creates a predictable, physics-driven world. It governs everything: how much damage a weapon does, how much support a pillar can provide, and how sound travels. It is the core of our simulation.

#### **2.2. Pillar 2: Acoustic Mass & Resonance (The "Echolocation" System)**
*   **The What:** Sound is not an abstract event; it is a physical phenomenon. A sound event generates a cloud of massless "Phonon" particles, each with a quantifiable `acoustic_mass`. These particles travel through the world, losing mass over distance, and creating sound upon impact with a collidable object.
*   **The Why:** This unifies sound design with the core physics engine, creating a deeply immersive and realistic 3D audio environment. The sound of rain on a tin roof is different from rain on mud because the *material properties* of the roof and mud react differently to the "weight" of the raindrop's sound.

#### **2.3. Pillar 3: Structural Integrity & Weight Distribution**
*   **The What:** The base building system is a direct extension of the core principle. Every building piece has a `mass` and a `load_bearing_capacity`. A structure will stand only if the pieces below it can support the cumulative weight of the pieces above them.
*   **The Why:** This makes engineering a real gameplay challenge. Players cannot build impossibly large structures on flimsy foundations. Sieges become more tactical, as destroying a single, critical support pillar can bring an entire tower crashing down in a satisfying, physics-based cascade.

#### **2.4. Pillar 4: Intelligent Rendering & Photography-Inspired Lighting**
*   **The What:** The renderer is built to make our physical world beautiful. It leverages aggressive culling, multi-tiered LODs, and a "Progressive Refinement" system that uses idle processing power to enhance shadow and light quality when the player is still, rewarding observation.
*   **The Why:** This allows us to achieve moments of breathtaking, "screenshot-worthy" beauty without needing to render at that quality 100% of the time, keeping the engine lightweight.

#### **2.5. Pillar 5: LLM-Assisted Architecture & Radical Modularity**
*   **The What:** The engine is built from discrete, modular components with clean APIs. This modularity is designed specifically for LLM integration. We will create data-driven systems where an LLM can easily generate content (items, quests, lore) that fits into pre-defined, validated templates.
*   **The Why:** This is our force multiplier. It allows a small, creative team to generate a vast, rich world by offloading the creation of structured data to an AI partner, while the human developer focuses on the core systems and creative vision.

```

### File: `/01_ENGINE_DESIGN/02_ENGINE_MODULES/09_Asset_Pipeline.md`
```md
# Engine Module: Asset Pipeline

## **1.0. Module Overview**

The **Asset Pipeline** is the engine's data preparation and management system. Its responsibility is to take raw, source-format assets (like `.png` textures, `.obj` models, or `.wav` sounds) and convert them into a clean, optimized, engine-native format that can be loaded into the game with maximum efficiency.

This module is not a single real-time system, but rather a combination of an **offline processing tool** and a run-time **Asset Manager**.

**Core Philosophy:** The engine at runtime should **never** have to deal with raw, unoptimized source files. Loading a `.png` and decompressing it on the fly is slow. Parsing a complex `.gltf` model file during a loading screen is inefficient. The Asset Pipeline does all this heavy lifting **ahead of time**, during the development process. The result is faster loading times, lower memory usage, and a smoother in-game experience.

## **2.0. The Two-Stage Process**

#### **Stage 1: The Offline Asset Processor (The "Cooker")**
This is a separate command-line tool that we will build. It is not part of the game executable. The developer runs this tool whenever new creative assets are added or changed.
*   **Function:** It scans a "raw_assets" directory, finds any new or modified files, and processes them.
    *   **For Textures:** It might convert a large `.png` file into a compressed texture format (like `.dds`) and generate mipmaps (smaller versions of the texture for objects in the distance).
    *   **For 3D Models:** It will parse the complex `.obj` or `.gltf` file and convert it into a simple, engine-native binary format that contains only the vertex and indexx data the GPU needs, organized for optimal memory layout.
    *   **For Audio:** It will convert a large `.wav` file into a compressed format like `.ogg`.
*   **Output:** The Processor outputs these optimized, "cooked" files into a "packaged_assets" directory that will be shipped with the final game. It also generates a master "asset manifest" file, which is a list of all available assets and where to find them.

#### **Stage 2: The Runtime Asset Manager**
This is the module that runs inside the game engine.
*   **Function:** Its job is simple: load the "cooked" assets from the packaged directory into memory when they are needed.
*   **Responsibilities:**
    *   **Loading & Unloading:** Provides the API for the rest of the engine to request an asset.
    *   **Reference Counting:** It keeps track of how many systems are currently using a specific asset. When an asset is no longer needed by anyone (e.g., leaving a level), its memory is freed up. This prevents memory leaks.
    *   **Asset Pooling:** It ensures that the same asset is never loaded into memory more than once. If three different enemies use the same "goblin.png" texture, the Asset Manager loads it once and gives all three of them a pointer to the same piece of memory.

## **3.0. Asset Naming and ID System**

To keep things simple and human-readable, an asset's unique identifier **(AssetID)** will simply be its relative file path from the root assets directory. This is an intuitive and powerful way to manage assets without needing complex ID numbers.

*   **Example AssetIDs:**
    *   `"textures/armor/iron_plate_albedo.dds"`
    *   `"models/characters/player.mesh"`
    *   `"audio/sfx/weapons/sword_swing.ogg"`
    *   `"fonts/main_menu_font.ttf"`

## **4.0. Module API Functions (The Runtime Asset Manager)**

These functions provide a clean interface for the rest of the engine to request assets without needing to know about the underlying file system or cooking process.

*   **Function: `Assets.Load(assetID)`**
    *   **Description:** The primary generic loading function. The Asset Manager will determine the asset type based on its file extension or manifest data and load it into the correct memory pool (texture memory, vertex buffer, etc.).
    *   **Parameters:** `assetID` (AssetID, a string path).
    *   **Returns:** `bool` (success). This function works asynchronously in the background.

*   **Function: `Assets.Unload(assetID)`**
    *   **Description:** Decrements the reference count for an asset. If the count reaches zero, the asset is removed from memory.
    *   **Parameters:** `assetID` (AssetID).
    *   **Returns:** `void`.

*   **Function: `Assets.IsLoaded(assetID)`**
    *   **Description:** A quick check to see if an asset has finished its background loading and is ready to be used.
    *   **Parameters:** `assetID` (AssetID).
    *   **Returns:** `bool`.

*   **Function: `Assets.Get(assetID)`**
    *   **Description:** Returns a handle or pointer to the actual asset data in memory that can be passed to other modules like the Renderer or Audio Engine. Will fail if `Assets.IsLoaded()` is false.
    *   **Parameters:** `assetID` (AssetID).
    *   **Returns:** `AssetHandle` (an internal engine object or pointer).

This pipeline creates a robust, professional workflow. Artists and designers can work with standard, user-friendly file formats, and the automated "cooker" ensures that the game engine only ever has to deal with perfectly optimized, ready-to-use data.
```

### File: `/01_ENGINE_DESIGN/02_ENGINE_MODULES/08_UI_System.md`
```md
# Engine Module: UI System

## **1.0. Module Overview**

The **UI System** is responsible for rendering and managing all User Interface elements, from the in-game Heads-Up Display (HUD) to complex inventory screens and dialogue boxes. This module translates game data (like player health or item lists) into visual elements (health bars, icons) that the player can understand and interact with.

**Core Philosophy:** Our UI system will be **declarative and data-driven**. We will avoid "hard-coding" UI layouts in the game logic. Instead, we will define the structure, position, and appearance of our UI in external data files (like XML or a custom format). The UI System's job is to read these layout files, create the corresponding elements, and update them based on the game's state. This makes iteration and redesign dramatically faster.

## **2.0. Key Responsibilities**

*   **Widget Rendering:** To render a variety of standard UI elements ("widgets"), such as panels, buttons, text labels, sliders, and progress bars.
*   **Layout Management:** To parse layout files and position widgets on the screen correctly, handling different screen resolutions and aspect ratios gracefully.
*   **Input Handling:** To process mouse clicks and keyboard navigation within UI screens, determining which widget is being interacted with. It will capture input so that clicks on the UI don't affect the game world behind it.
*   **State Management:** To manage which UI "screens" are currently active (e.g., Inventory, Map, Pause Menu) and handle the transitions between them.
*   **Data Binding:** To link UI elements to live game data. For example, a "Health Bar" widget will be bound to the player's health attribute, automatically updating its visual state as the player takes damage.

## **3.0. System Architecture: The Widget Tree**

The UI will be structured as a **tree of widgets**. This hierarchical system allows for complex layouts to be built from simple components.

*   **Canvas (The Root):** The root of every UI screen. It covers the entire screen and all other widgets are its "children."
*   **Panel (The Container):** An invisible container used to group other widgets. A panel can be used to create a "window" for an inventory screen or a "row" for hotbar slots.
*   **Widget (The Element):** The individual, visible elements.
    *   **Text Label:** Displays static or dynamic text.
    *   **Image/Icon:** Displays a static texture.
    *   **Button:** An interactable image or text that triggers an event when clicked.
    *   **Progress Bar:** A bar that can be filled, used for health, stamina, or loading indicators.
    *   **Slider:** A control for adjusting a value, used in settings menus.
    *   **Grid:** A container that automatically arranges its children into a grid, perfect for inventory slots.

**Example Layout (Declarative pseudo-code):**
```xml
<Canvas>
  <Panel id="PlayerHUD" position="bottom-left">
    <ProgressBar id="HealthBar" binding="Player.Health" size="200, 20" />
    <ProgressBar id="StaminaBar" binding="Player.Stamina" position="0, 25" size="150, 15" />
  </Panel>
  <Panel id="PauseMenu" visible="false">
    <Button text="Resume" onClick="StateManager.SetState(IN_GAME)" />
    <Button text="Quit" onClick="Engine.Shutdown()" />
  </Panel>
</Canvas>
```
The UI system parses this "code," creates the widgets, and handles their visibility and events.

## **4.0. Module API Functions**

The game logic will interact with the UI system through a high-level API, mostly for showing/hiding screens and sending events.

*   **Function: `UI.LoadScreen(layoutFile)`**
    *   **Description:** Loads a UI layout file from disk and creates the widget tree, but does not display it yet.
    *   **Parameters:** `layoutFile` (string, e.g., `"layouts/hud.xml"`).
    *   **Returns:** `ScreenID`.

*   **Function: `UI.ShowScreen(screenID)`**
    *   **Description:** Makes a loaded screen visible and active, adding it to the update/render list.
    *   **Parameters:** `screenID` (ScreenID).

*   **Function: `UI.HideScreen(screenID)`**
    *   **Description:** Hides a screen, deactivating it.
    *   **Parameters:** `screenID` (ScreenID).

*   **Function: `UI.SendEvent(eventName, data)`**
    *   **Description:** A way for game logic to send data or trigger animations in the UI. For example, when the player picks up an item, the game logic would call `UI.SendEvent("PlayerInventoryUpdated", { ...new inventory data... })`. The UI system then ensures any visible inventory screen updates itself.
    *   **Parameters:** `eventName` (string), `data` (Object).

*   **Function: `UI.BindData(widgetID, data_source)`**
    *   **Description:** A lower-level function used during layout loading to link a widget's property (like a progress bar's `fill_amount`) to a source of game data. This is the heart of the data-binding system.
    *   **Parameters:** `widgetID` (string), `data_source` (Object/function pointer).

This architecture creates a powerful, flexible, and decoupled UI system that is easy to iterate on without needing to constantly recompile game code. We can change the entire layout of the main menu just by editing a single text file.
```

### File: `/01_ENGINE_DESIGN/02_ENGINE_MODULES/07_Audio_Engine.md`
```md
# Engine Module: Audio Engine

## **1.0. Module Overview**

The **Audio Engine** is the soul and voice of the Stelliferrum Forge. Its responsibility is to manage and play all sound within the game world, from the quietest footstep to the most thunderous explosion and the most sweeping musical score. This module's primary design goals are to create a **deeply immersive ambient soundscape** and to provide a **dynamic, responsive musical experience.**

**Core Philosophy:** Audio is a key driver of emotion and player feedback. Our engine will treat sound with the same level of importance as graphics. We will focus on creating a high-fidelity experience, particularly for environmental audio like rain and wind, and a music system that adapts seamlessly to the player's actions. We will almost certainly use a robust third-party audio library (like **FMOD** or **Wwise**) as a backend to handle the complex mixing and effects, while our engine code will act as the "director," telling the library what to play and when.

## **2.0. Key Responsibilities**

*   **Sound Playback:** To play, pause, stop, and loop both 2D (UI) and 3D (world-space) sounds.
*   **3D Positional Audio:** To accurately simulate the position of a sound in 3D space. A sound originating from the left should be heard in the left speaker.
*   **Attenuation (Distance):** To decrease the volume of a sound as the player moves further away from its source. This is a critical feature you requested.
*   **Dynamic Music System:** To manage and transition between different musical "states" based on the gameplay context (e.g., Exploration, Combat, Boss Fight).
*   **Audio Mixing & Effects:** To manage different audio channels (e.g., Music, SFX, Dialogue) and apply environmental effects like reverb in caves or muffling sounds through walls.

## **3.0. Dynamic & Ambient Sound Systems**

#### **3.1. The Ambiance & Weather System**
This is a top priority. The goal is to make the player *feel* the environment through sound.
*   **Layered Ambiance:** The background sound will be constructed from multiple layers. For example, a forest might have:
    *   `Layer 1: Base Wind` (a constant, gentle air tone)
    *   `Layer 2: Foliage Rustle` (the sound of wind in the trees, which gets louder as the wind picks up)
    *   `Layer 3: Distant Wildlife` (periodic, randomized bird calls or insect chirps)
*   **Dynamic Rain:** Your core request. Rain will not be a single sound file. It will be a dynamic, multi-layered system.
    *   **Light Drizzle:** A soft, high-frequency "hiss."
    *   **Heavy Rain:** Adds a deeper, more powerful layer with more bass.
    *   **Surface Impacts:** A separate layer of sound will be dedicated to the sound of raindrops hitting the surface the player is standing under. This is key. The sound of rain on a tent roof will be different from the sound of it on a metal roof, which will be different from the sound of it on forest leaves.
    *   **Indoor Muffling:** When the player enters an enclosed space, the "exterior" rain layers will be heavily muffled and low-passed, while the "interior" impact layer on the roof becomes the dominant sound. This creates a powerful sense of shelter.

#### **3.2. The Dynamic Music System**
This system uses a "state machine" to transition between musical cues seamlessly.
*   **Music States:**
    *   **`Exploration`:** Calm, atmospheric, and often minimalist music that complements the current biome.
    *   **`Tension`:** Triggered when a single enemy is alerted but has not yet fully detected the player. A low, pulsing bassline or a single sustained string note is added to the Exploration track.
    *   **`Combat (Standard)`:** Triggered when the Hunting state begins. A percussive, high-energy track with multiple layers kicks in. As more enemies join the fight, more layers (e.g., more drums, brass stabs) are added to increase the intensity.
    *   **`Combat (Boss)`:** A unique, epic track specifically composed for each major boss encounter.
*   **Transitions:** The system will use intelligent transitions (e.g., a "sting" like a cymbal crash or a drum fill) to move between states without feeling jarring. When combat ends, the music will fade to an "outro" stem before gracefully returning to the Exploration track.

## **4.0. Module API Functions**

*   **Function: `Audio.PlaySound2D(assetID, volume)`**
    *   **Description:** Plays a simple, non-positional sound. Used for UI elements like button clicks.
    *   **Parameters:** `assetID` (AssetID), `volume` (float).

*   **Function: `Audio.PlaySound3D(assetID, position, volume, radius)`**
    *   **Description:** Plays a sound effect at a specific location in the 3D world.
    *   **Parameters:**
        *   `assetID` (AssetID).
        *   `position` (Vector3): The world coordinate of the sound's source.
        *   `volume` (float).
        *   `radius` (float): The distance at which the sound will no longer be audible (attenuation).

*   **Function: `Audio.PlayMusic(trackID, fade_duration)`**
    *   **Description:** A high-level command. Tells the Dynamic Music System to transition to a new track or state (e.g., `trackID` could be `"Combat_Orcs"`).
    *   **Parameters:** `trackID` (string), `fade_duration` (float, in seconds).

*   **Function: `Audio.SetMusicState(newState)`**
    *   **Description:** The primary function for dynamic music. Tells the system to shift its intensity.
    *   **Parameters:** `newState` (enum, e.g., `MUSIC_STATE_EXPLORE`, `MUSIC_STATE_TENSION`, `MUSIC_STATE_COMBAT`).

*   **Function: `Audio.SetGlobalParameter(paramName, value)`**
    *   **Description:** A powerful function for controlling the overall audio mix.
    *   **Parameters:**
        *   `paramName` (string, e.g., `"IsInside"`, `"RainIntensity"`).
        *   `value` (float, e.g., `1.0` for true, `0.75` for heavy rain).
    *   **Example Usage:** `Audio.SetGlobalParameter("IsInside", 1.0);` // This would tell the audio backend (FMOD/Wwise) to apply the "muffled" effect to all outdoor sounds.
```

### File: `/01_ENGINE_DESIGN/02_ENGINE_MODULES/06_Physics_Engine.md`
```md
# Engine Module: Physics Engine

## **1.0. Module Overview**

The **Physics Engine** is responsible for simulating the physical laws of the game world. It manages motion, collision detection, and collision resolution for all relevant game objects. This module is what makes a sword strike feel impactful, a fall feel dangerous, and a "Telekinesis" spell feel powerful.

**Core Philosophy:** Our physics engine is built for **performance and gameplay feel, not perfect scientific accuracy.** We will prioritize fast, stable, and predictable physics that support our game's mechanics, particularly the dynamic magic system. We will likely use a lightweight, established third-party physics library (like **Box2D** for 2D, or a simplified 3D library) as a foundation and build our gameplay-specific logic on top of it. This follows our philosophy of not reinventing the wheel for complex, universal problems.

## **2.0. Key Responsibilities**

*   **Rigid Body Simulation:** To manage the state of all physical objects ("bodies"), including their position, rotation, velocity, and mass.
*   **Collision Shape Management:** To associate each physical body with a simplified collision shape (e.g., box, sphere, capsule, polygon mesh) for fast and efficient collision checks.
*   **Collision Detection:** To identify when the collision shapes of two or more objects are intersecting. This is the most computationally expensive part of the simulation.
*   **Collision Resolution:** To calculate and apply the appropriate response to a collision, such as making objects bounce off each other or applying damage.
*   **Force & Impulse Application:** To provide a simple API for other systems to apply forces (a push over time) and impulses (an instantaneous "kick") to objects. This is the primary way the rest of the engine interacts with the physics simulation.
*   **Callbacks & Events:** To notify the game logic when a collision occurs (e.g., "Player's sword just hit Enemy #5").

## **3.0. The Physics "World" & Simulation Loop**

The Physics Engine maintains its own internal representation of the world, often called a "physics world" or "scene." This world only contains the physical properties of objects, not their visual models or game logic.

1.  **Synchronization:** At the beginning of each frame's update, the game logic updates the state of any "kinematic" or player-controlled bodies in the physics world.
2.  **Simulation Step (`Physics.Update()`):** The engine then calls the main `Update` function of the physics module. This function advances the simulation forward by a fixed timestep (`deltaTime`). Inside this step, the physics library performs its "black box" magic: it applies gravity, detects all collisions, and resolves them.
3.  **Callbacks:** During the simulation step, if a collision occurs that the game logic has "subscribed" to, the Physics Engine will immediately call back to the game logic, passing it information about the collision. This is how we apply damage.
4.  **Data Retrieval:** After the simulation step is complete, the `Renderer` and other modules can then query the Physics Engine (`Physics.GetPosition()`) to get the new, updated positions and rotations of all dynamic objects so they can be drawn correctly.

## **4.0. Module API Functions**

These public-facing functions allow the game to set up, manipulate, and query the physics simulation.

*   **Function: `Physics.CreateBody(entityID, body_definition)`**
    *   **Description:** The primary function for adding a new object to the physics world.
    *   **Parameters:**
        *   `entityID` (EntityID): The unique identifier for the game entity this body represents.
        *   `body_definition` (Object): A data structure containing all necessary information, such as:
            *   `type`: (e.g., "static", "dynamic", "kinematic")
            *   `position`: (Vector3)
            *   `shape`: (e.g., `{type:'box', size:{x,y,z}}` or `{type:'sphere', radius:r}`)
            *   `mass`: (float)
            *   `friction`: (float)
            *   `restitution`: (float, "bounciness")
    *   **Returns:** `bool` (success).

*   **Function: `Physics.DestroyBody(entityID)`**
    *   **Description:** Removes an object's physical body from the simulation.
    *   **Parameters:** `entityID` (EntityID).
    *   **Returns:** `void`.

*   **Function: `Physics.ApplyForce(entityID, forceVector, pointOfApplication)`**
    *   **Description:** Applies a continuous force to the center of mass of a dynamic body.
    *   **Parameters:** `entityID` (EntityID), `forceVector` (Vector3). `pointOfApplication` (Vector3, optional).

*   **Function: `Physics.ApplyImpulse(entityID, impulseVector, pointOfApplication)`**
    *   **Description:** Applies an instantaneous "kick" to a dynamic body. Used for explosions, weapon impacts, and jumps.
    *   **Parameters:** `entityID` (EntityID), `impulseVector` (Vector3). `pointOfApplication` (Vector3, optional).

*   **Function: `Physics.SetTransform(entityID, position, rotation)`**
    *   **Description:** Manually overrides the position and rotation of a physics body. Used for teleporting or setting the position of player-controlled characters.
    *   **Parameters:** `entityID` (EntityID), `position` (Vector3), `rotation` (Quaternion/Vector3).

*   **Function: `Physics.GetTransform(entityID)`**
    *   **Description:** Retrieves the current position and rotation of a physics body after the simulation step.
    *   **Parameters:** `entityID` (EntityID).
    *   **Returns:** `Object` `{position: Vector3, rotation: Quaternion/Vector3}`.

*   **Function: `Physics.Raycast(startPoint, endPoint)`**
    *   **Description:** Casts a virtual line (a "ray") from a start point to an end point and returns the first object it hits. Essential for things like bullet detection or determining what the player is looking at.
    *   **Parameters:** `startPoint` (Vector3), `endPoint` (Vector3).
    *   **Returns:** `Object` `{hit: bool, entityID: EntityID, hitPoint: Vector3}`.
```

### File: `/01_ENGINE_DESIGN/02_ENGINE_MODULES/05_3D_Renderer.md`
```md
# Engine Module: 3D Renderer

## **1.0. Module Overview**

The **3D Renderer** is the evolutionary next step for the Stelliferrum Forge's visual capabilities. Its responsibility is to render complex 3D models, manage a 3D camera, and, most importantly, implement the **world-class lighting engine** that is a core pillar of our design philosophy. This module will eventually replace the `2D_Renderer` for all in-world rendering, though the 2D module may still be used for UI overlays.

**Core Philosophy:** Our 3D renderer is not a "brute-force" engine. It is an **"Intelligent Renderer"** that uses clever, modern techniques to achieve breathtaking visuals on a lightweight framework. Our primary focus is on the **artistry of light and shadow**, not on rendering an arbitrarily high number of polygons.

## **2.0. Phased Development Roadmap**

The development of this module will occur in clear, iterative phases. Each phase will build upon the last, ensuring we always have a functional base.

*   **Phase 1: The Basics** - Getting a 3D model on screen.
*   **Phase 2: The World** - Rendering a simple landscape and implementing culling/LODs.
*   **Phase 3: The Light** - Implementing the core lighting model. This is the most critical phase.
*   **Phase 4: The Beauty** - Adding advanced post-processing and the "Progressive Refinement" system.

## **3.0. Key Systems & Responsibilities**

#### **3.1. 3D Model & Mesh Handling**
*   **Responsibility:** To load 3D model data (vertices, normals, UVs) from standard file formats (like `.obj` or `.gltf`).
*   **Functionality:** Will manage vertex buffers, indexx buffers, and send this geometric data to the GPU for rendering.

#### **3.2. Material & Texture System**
*   **Responsibility:** To manage the "surfaces" of 3D models. A material defines how a surface reacts to light.
*   **Functionality:** A material will be a collection of textures:
    *   **Albedo/Diffuse Map:** The base color of the object.
    *   **Normal Map:** Adds the illusion of fine surface detail (like bumps and scratches) without adding more polygons.
    *   **Metallic/Roughness Maps:** The core of Physically-Based Rendering (PBR), defining how metallic a surface is and how polished it is.

#### **3.3. 3D Camera System**
*   **Responsibility:** To manage the player's viewpoint in 3D space.
*   **Functionality:** Will control the camera's position, rotation (pitch/yaw), and Field of View (FOV). It generates the "View" and "Projection" matrices that tell the GPU how to transform 3D world coordinates into a 2D image.

#### **3.4. The Lighting Engine (The Crown Jewel)**
*   **Responsibility:** To simulate the interaction of light with the world's surfaces. This is our area of excellence.
*   **Functionality:**
    *   **Light Types:** Will support different types of lights, each with its own properties:
        *   `Directional Light`: A single, infinitely distant light source used to simulate the sun or moon.
        *   `Point Light`: A light that radiates outwards from a single point, like a torch or a lantern.
        *   `Spot Light`: A cone of light, like a flashlight.
    *   **Shadow Mapping:** A core technique for generating dynamic shadows from our light sources.
    *   **PBR Shaders:** The lighting calculations will adhere to Physically-Based Rendering principles, ensuring materials look realistic and consistent under different lighting conditions.

#### **3.5. Intelligent Culling & LOD System**
*   **Responsibility:** To ensure we are not trying to render the entire world every frame.
*   **Functionality:**
    *   **Frustum Culling:** Objects outside the camera's view cone are not drawn.
    *   **Occlusion Culling:** Objects hidden behind other objects (like a mountain) are not drawn.
    *   **Level of Detail (LODs):** Manages the swapping of high-poly models for low-poly versions at a distance.
    *   **Impostors:** Manages the final swap from a 3D model to a 2D image for objects on the far horizon.

## **4.0. Module API Functions (Conceptual)**

The 3D Renderer's API will be more complex, centered on a "Scene Graph" or a similar entity-component system. Here is a high-level concept of its functions.

*   **Function: `Renderer3D.SubmitStaticMesh(modelID, materialID, transform)`**
    *   **Description:** Submits a static (unmoving) 3D model to the scene to be rendered.
    *   **Parameters:**
        *   `modelID` (AssetID): The identifier for the loaded 3D model.
        *   `materialID` (AssetID): The identifier for the material to apply.
        *   `transform` (Matrix4x4): The model's position, rotation, and scale in the world.
    *   **Returns:** `EntityID`.

*   **Function: `Renderer3D.UpdateDynamicMesh(entityID, transform)`**
    *   **Description:** Updates the position/rotation of a moving entity for the next frame.

*   **Function: `Renderer3D.CreatePointLight(position, color, radius, intensity)`**
    *   **Description:** Adds a new point light to the lighting simulation.
    *   **Returns:** `LightID`.

*   **Function: `Renderer3D.UpdateDirectionalLight(direction, color, intensity)`**
    *   **Description:** Updates the properties of the main sun/moon light source, used for the day/night cycle.

*   **Function: `Renderer3D.SetCamera(position, rotation, FOV)`**
    *   **Description:** Sets the camera's properties for the next frame.

This architectural plan lays the foundation for a powerful and intelligent rendering system, capable of delivering on the project's ambitious visual goals through smart design rather than sheer brute force.
```

### File: `/01_ENGINE_DESIGN/02_ENGINE_MODULES/04_2D_Renderer.md`
```md
# Engine Module: 2D Renderer

## **1.0. Module Overview**

The **2D Renderer** is the primary graphics module for the initial versions of the Stelliferrum Forge. Its responsibility is to take abstract drawing commands (e.g., "draw this sprite at this position") and translate them into low-level instructions that the GPU can understand and display on the screen. It is the "Anvil" upon which our game's visual identity will be forged.

**Core Philosophy:** The renderer should be simple, efficient, and versatile. Our initial goal is not complex 3D scenes, but a highly optimized pipeline for drawing thousands of 2D sprites (for characters, items, and UI) and text elements per frame. This forms the foundation for all future 3D enhancements.

## **2.0. Key Responsibilities**

*   **Render Pipeline Management:** To control the entire sequence of a render frame, from clearing the screen to presenting the final image.
*   **Sprite Batching:** To group thousands of individual draw calls into a small number of large "batches." This is the single most important optimization for a 2D renderer. Instead of telling the GPU "draw this sprite, now this sprite, now this sprite...", we tell it "draw all 500 of these sprites at once."
*   **Camera & Coordinate Systems:** To manage the 2D camera, which determines what part of the "world" is visible. It will handle the translation between world coordinates (where a character is in the game world) and screen coordinates (where it is drawn in the window).
*   **Shader Management:** To load, compile, and apply simple GLSL/HLSL shader programs. Initially, this will be a basic shader for drawing textured sprites, but this system will be the gateway to all future advanced lighting and visual effects.
*   **Text Rendering:** To take text strings and render them to the screen using loaded font atlases.

## **3.0. The Rendering Pipeline (Simplified)**

Within the main game loop, the renderer's job is split into three phases:

1.  **`Renderer.BeginFrame()`:** Called once at the start of the render phase. This function prepares the GPU by:
    *   Clearing the previous frame's image (e.g., setting the background to black).
    *   Setting up the camera's view matrix based on its position and zoom.
    *   Starting a new "batch" for drawing sprites.

2.  **Drawing Commands (`DrawSprite`, `DrawText`, etc.):** Throughout the render phase, other game systems will call the renderer's public functions. These functions do not immediately draw to the screen. Instead, they add the sprite's data (position, texture, color) to the current batch in memory.

3.  **`Renderer.EndFrame()`:** Called once at the end of the render phase. This is where the real work happens.
    *   **Flush Batch:** The renderer takes the entire batch of sprite data that was collected during the frame and sends it to the GPU in a single, large draw call.
    *   **Swap Buffers:** Calls `Platform.SwapBuffers()` to present the newly drawn image to the screen.

## **4.0. Module API Functions**

These are the public-facing functions that the game logic and state manager will use to draw things.

*   **Function: `Renderer.BeginFrame()`**
    *   **Description:** Prepares for a new frame. Clears the screen and sets up the camera.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function: `Renderer.EndFrame()`**
    *   **Description:** Flushes any pending draw calls and presents the final image to the window.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function: `Renderer.DrawSprite(assetID, position, size, options)`**
    *   **Description:** The primary workhorse function. Adds a sprite to the current rendering batch.
    *   **Parameters:**
        *   `assetID` (AssetID): The unique identifier for the loaded texture.
        *   `position` (Vector2): The world-space coordinate `{x, y}` for the sprite's center.
        *   `size` (Vector2): The `{width, height}` of the sprite in world units.
        *   `options` (Object, optional): A collection of optional parameters like:
            *   `rotation` (float, default=`0`): Rotation in degrees.
            *   `color_tint` (Color, default=`white`): A color to tint the sprite.
            *   `z_indexx` (int, default=`0`): A layer indexx to control drawing order (higher numbers are drawn on top).
    *   **Returns:** `void`.

*   **Function: `Renderer.DrawRect(position, size, color, is_filled)`**
    *   **Description:** Adds a simple, untextured rectangle to the render batch. Useful for debugging and simple UI backgrounds.
    *   **Parameters:**
        *   `position` (Vector2), `size` (Vector2), `color` (Color).
        *   `is_filled` (bool, optional, default=`true`): If false, it draws only the outline.
    *   **Returns:** `void`.

*   **Function: `Renderer.DrawText(text_string, position, options)`**
    *   **Description:** Adds text to be rendered. This often uses a separate rendering path from sprites.
    *   **Parameters:**
        *   `text_string` (string).
        *   `position` (Vector2): The screen-space pixel coordinate for the text's top-left.
        *   `options` (Object, optional):
            *   `font_id` (AssetID).
            *   `font_size` (int, default=`16`).
            *   `color` (Color, default=`white`).
    *   **Returns:** `void`.

*   **Function: `Renderer.SetCamera(position, zoom)`**
    *   **Description:** Controls the camera for world-space rendering.
    *   **Parameters:**
        *   `position` (Vector2): The world coordinate the camera should center on.
        *   `zoom` (float, default=`1.0`): The camera's zoom level. >1 zooms in, <1 zooms out.
    *   **Returns:** `void`.
```

### File: `/01_ENGINE_DESIGN/02_ENGINE_MODULES/03_Input_Handler.md`
```md
# Engine Module: Input Handler

## **1.0. Module Overview**

The **Input Handler** is the engine's central nervous system. Its sole responsibility is to process the raw hardware input events captured by the `Platform` module and translate them into a simple, queryable state that the rest of the game can easily understand. It answers the fundamental questions of gameplay: "Is the 'W' key down?", "Was the left mouse button just clicked?", "Where is the cursor?"

**Core Philosophy:** The game logic should never have to worry about low-level hardware events or scancodes. The Input Handler abstracts all of this away. The game simply asks for the *state* of an action, and this module provides a clean, reliable answer.

## **2.0. Key Responsibilities**

*   **State Tracking:** To maintain the current state of every key on the keyboard and every button on the mouse for the current frame.
*   **"Pressed" and "Released" Logic:** To differentiate between a key being *held down* and a key being *pressed for the first time*. This is critical for gameplay; "holding" W moves the player forward, while a single "press" of Spacebar makes them jump.
*   **Mouse Position Tracking:** To keep an up-to-date record of the mouse cursor's X and Y coordinates.
*   **Action Mapping (Future Goal):** To eventually support a layer of abstraction where a physical key (e.g., `"Space"`) can be mapped to a logical game action (e.g., `"JUMP"`). This will be essential for implementing key-binding options for the player. For now, we will work with direct key codes.

## **3.0. Implementation Details**

The Input Handler operates in a two-step process within the main game loop.

1.  **Event Processing (The "Update" Phase):** At the beginning of each frame's update cycle, the `Input.ProcessNewEvents()` function is called. It takes the queue of raw events from `Platform.PollEvents()` (e.g., "Key 87 Down," "Key 87 Up"). It updates its internal arrays that track the state of all keys. A key part of this process is comparing the current frame's state to the previous frame's state to determine if a key was *just* pressed or *just* released.
2.  **Querying (The "Access" Phase):** Throughout the rest of the game logic update, other systems (like the Player Controller) can then call the public API functions (`Input.IsKeyDown()`, etc.) to get the clean, processed state for the current frame.

This ensures that the state of all inputs is consistent for the entire duration of a single game logic update.

## **4.0. Module API Functions**

These are the public-facing functions that the game logic will use to query the player's actions.

#### **Keyboard Functions**
*   **Function: `Input.IsKeyDown(keyCode)`**
    *   **Description:** Returns `true` for every frame that a specific key is held down. Ideal for continuous actions like movement.
    *   **Parameters:** `keyCode` (string, e.g., `"W"`, `"Left Shift"`).
    *   **Returns:** `bool`.

*   **Function: `Input.IsKeyPressed(keyCode)`**
    *   **Description:** Returns `true` only on the *single frame* that a key is first pressed down. Essential for discrete actions like jumping, interacting, or firing a semi-automatic weapon.
    *   **Parameters:** `keyCode` (string).
    *   **Returns:** `bool`.

*   **Function: `Input.IsKeyReleased(keyCode)`**
    *   **Description:** Returns `true` only on the *single frame* that a key is released. Useful for actions that trigger on release, like charging a bow shot.
    *   **Parameters:** `keyCode` (string).
    *   **Returns:** `bool`.

#### **Mouse Functions**
*   **Function: `Input.IsMouseButtonDown(buttonCode)`**
    *   **Description:** Returns `true` while a mouse button is held down.
    *   **Parameters:** `buttonCode` (int, `0`=Left, `1`=Right, `2`=Middle).
    *   **Returns:** `bool`.

*   **Function: `Input.IsMouseButtonPressed(buttonCode)`**
    *   **Description:** Returns `true` only on the single frame that a mouse button is first clicked.
    *   **Parameters:** `buttonCode` (int).
    *   **Returns:** `bool`.

*   **Function: `Input.GetMousePosition()`**
    *   **Description:** Returns the current (X, Y) pixel coordinates of the mouse cursor within the game window.
    *   **Parameters:** None.
    *   **Returns:** `Vector2`.

*   **Function: `Input.GetMouseDelta()`**
    *   **Description:** Returns the change in mouse position since the last frame. Essential for implementing camera controls in a first-person or third-person perspective.
    *   **Parameters:** None.
    *   **Returns:** `Vector2` `{deltaX, deltaY}`.

*   **Function: `Input.GetMouseWheelScroll()`**
    *   **Description:** Returns the amount the mouse wheel was scrolled this frame (e.g., `+1` for scrolled up, `-1` for scrolled down).
    *   **Parameters:** None.
    *   **Returns:** `int`.
```

### File: `/01_ENGINE_DESIGN/02_ENGINE_MODULES/02_Platform_and_Windowing.md`
```md
# Engine Module: Platform and Windowing

## **1.0. Module Overview**

The **Platform and Windowing Module** is the lowest-level component of the Stelliferrum Forge. Its sole responsibility is to handle direct communication with the host **Operating System (OS)**. It abstracts away the platform-specific complexities of creating and managing a window, handling basic OS messages, and providing a stable rendering context for the rest of the engine.

This module is the first thing that gets initialized and the last thing that gets shut down. Everything the player sees happens inside the window that this module creates.

**Core Philosophy:** The rest of the engine should be as "platform-agnostic" as possible. The `Renderer` should not need to know if it's drawing to a Windows window or a Linux window; it only needs a valid drawing surface. This module provides that universal surface.

## **2.0. Key Responsibilities**

*   **Window Creation:** To create a native OS window with a specified title, size, and style (e.g., bordered, borderless, fullscreen).
*   **Rendering Context:** To initialize and manage the low-level graphics context (e.g., OpenGL, Vulkan, DirectX) that the `Renderer` module will use to draw.
*   **Event Pumping:** To process the OS message queue each frame. This includes handling events like the user clicking the "X" button to close the window, window resizing, or the window losing/gaining focus.
*   **Input Forwarding:** To capture raw hardware input events (keyboard presses, mouse movement) from the OS and forward them to the higher-level `Input Handler` module for processing.
*   **Buffer Swapping:** To take the final, completed image that the `Renderer` has drawn and present it to the screen.

## **3.0. Implementation Details (The "Behind the Scenes")**

While the rest of the engine will use our simple, abstract API, this module will be built using a low-level, third-party library to handle the platform-specific details. A library like **SDL (Simple DirectMedia Layer)** or **GLFW** is the ideal choice for this.

*   **Why use a library?** Writing windowing and input code from scratch for every OS (Windows, macOS, Linux) is a monumental, error-prone task that provides no direct gameplay value. Using a trusted, cross-platform library like SDL allows us to write our windowing code **once** and have it work everywhere.
*   **The Abstraction:** This module acts as a "wrapper" around the chosen library. Our engine calls `Platform.CreateWindow()`. Internally, the module translates that call into the specific `SDL_CreateWindow()` function. This means that if we ever wanted to change from SDL to a different library, we would only need to update the code *inside this one module*, and the rest of the engine would not be affected.

## **4.0. Module API Functions**

These are the public-facing functions that the `Engine` core and other modules will use to interact with the platform layer.

*   **Function: `Platform.Initialize(title, width, height, mode)`**
    *   **Description:** The primary initialization function. Creates the game window and sets up the graphics context.
    *   **Parameters:**
        *   `title` (string): The text to appear in the window's title bar.
        *   `width` (int): The initial width of the window in pixels.
        *   `height` (int): The initial height of the window in pixels.
        *   `mode` (enum, e.g., `WINDOWED`, `FULLSCREEN`, `BORDERLESS`): The initial window style.
    *   **Returns:** `bool` (success).

*   **Function: `Platform.Shutdown()`**
    *   **Description:** Destroys the window and cleans up the graphics context.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function: `Platform.PollEvents()`**
    *   **Description:** Called once per frame by the core loop. This function processes all pending OS messages. It is responsible for detecting the "quit" event and telling the engine to shut down.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function: `Platform.SwapBuffers()`**
    *   **Description:** Called at the very end of the rendering phase. It presents the back-buffer (what the renderer has been drawing to) to the screen.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function: `Platform.GetWindowSize()`**
    *   **Description:** Returns the current dimensions of the window's drawable area.
    *   **Parameters:** None.
    *   **Returns:** `Vector2` `{width, height}`.

This clean, focused module handles all the messy, low-level OS communication, providing the rest of the Stelliferrum Forge with a clean, stable foundation to build upon.
```

### File: `/01_ENGINE_DESIGN/02_ENGINE_MODULES/01_Core_Loop_and_State_Manager.md`
```md
# Engine Module: Core Loop and State Manager

## **1.0. Module Overview**

This module represents the central hub of the **Stelliferrum Forge**. It serves two distinct but inseparable functions:

1.  **The Core Loop:** Acts as the engine's main "heartbeat." It is a continuous loop that dictates the flow of execution for the entire application, ensuring every other module is updated in the correct sequence, frame after frame.
2.  **The State Manager:** Acts as the engine's "brain" or "director." It controls the high-level state of the game—whether we are in the Main Menu, playing the game, or viewing a loading screen. This ensures that only relevant systems are active at any given time.

## **2.0. The Core Game Loop**

The engine's operation is defined by a simple, repeating sequence of events. This loop will run as fast as the hardware allows, with its timing managed by `Engine.GetDeltaTime()` to ensure smooth, frame-rate-indexpendent operation.

The strict order of operations is as follows:

```
// --- Conceptual Pseudo-code of the Main Loop ---

Initialize_All_Engine_Modules();

// Set the initial game state.
StateManager.SetState(GameState.MAIN_MENU);

while (Engine.is_running) {
    // 1. INPUT
    // First, process all raw input from the OS.
    Input.ProcessEvents();
    
    // 2. UPDATE (The "Thinking" Phase)
    // Update the currently active game state.
    // The State Manager ensures only the logic for the correct state runs
    // (e.g., only updates the menu in the menu state, only updates the world in the game state).
    StateManager.Update(Engine.GetDeltaTime());
    
    // The StateManager's Update function will, in turn, call other module updates as needed.
    // For example, in the "In-Game" state, it will call:
    //   - World.Update(deltaTime);
    //   - Physics.Update(deltaTime);
    //   - Player.Update(deltaTime, Input);

    // 3. RENDER (The "Drawing" Phase)
    // This phase should ONLY contain drawing commands. No game logic.
    Renderer.BeginFrame();
    
    // Ask the State Manager what to draw.
    StateManager.Render();

    // The StateManager's Render function will call other rendering functions.
    // For example, in the "In-Game" state, it will call:
    //   - World.Render(Renderer);
    //   - Player.Render(Renderer);
    //   - UI.Render(Renderer);

    Renderer.EndFrame();
}

Shutdown_All_Engine_Modules();
```

## **3.0. The Game State Manager**

The State Manager is a **finite state machine**. It ensures the engine is always in one, and only one, high-level state. This is crucial for managing complexity and optimizing performance.

#### **3.1. Defined Game States**
*   **`STATE_INITIALIZING`:** The very first state. Loads critical assets and prepares the engine. Transitions automatically to `STATE_MAIN_MENU`.
*   **`STATE_MAIN_MENU`:** The player is on the main menu. In this state, only the UI and Input modules are significantly active. The physics and world simulation are paused.
*   **`STATE_LOADING_WORLD`:** A transition state shown when a new game is being generated or a save file is being loaded. Displays a loading screen.
*   **`STATE_IN_GAME`:** The primary state where the game is played. All engine modules are fully active: physics, rendering, AI, player logic, etc.
*   **`STATE_PAUSED`:** When the player opens the pause menu while in-game. The world simulation and physics are frozen, but the UI and Input systems are active to navigate the menu.
*   **`STATE_EXITING`:** The final state before shutdown. Saves game data and performs cleanup.

#### **3.2. State Manager API Functions**

These functions are part of a conceptual `StateManager` object.

*   **Function: `StateManager.SetState(newState)`**
    *   **Description:** The core function used to transition the engine from one state to another. This function will handle all necessary cleanup of the old state (e.g., unloading menu assets) and initialization of the new state (e.g., starting the physics simulation).
    *   **Parameters:** `newState` (GameState enum).
    *   **Returns:** `void`.

*   **Function: `StateManager.Update(deltaTime)`**
    *   **Description:** Called once per frame from the main loop. It contains a `switch` statement that calls the specific update logic for the *currently active state*.
    *   **Parameters:** `deltaTime` (float).
    *   **Returns:** `void`.

*   **Function: `StateManager.Render()`**
    *   **Description:** Called once per frame from the main loop. It contains a `switch` statement that calls the specific rendering logic for the *currently active state*.
    *   **Parameters:** None.
    *   **Returns:** `void`.

By cleanly separating the high-level states, we ensure that we're never trying to run player physics while in the main menu, or render the world while on a loading screen. This architecture is fundamental to a stable and professional engine.
```
