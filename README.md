<!-- Header Banner with Dark Slate to Terracotta Fluent Gradient -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:181B1E,28:242A30,58:5E2E23,82:A84C36,100:E07A5F&height=145&section=header&text=Ishan%20Shishodiya&fontSize=36&fontAlignY=38&fontColor=F7F6F2&desc=Systems%20Engineer%20%E2%86%92%20AI%20Research%20Engineer&descFontSize=16&descAlignY=65&descColor=F7F6F2&animation=fadeIn" width="100%" alt="Header Banner" />
  <br/>
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=15&pause=1200&color=E07A5F&center=true&vCenter=true&width=620&height=36&lines=Building+'MyTorch'%3A+C%2B%2B%2FCUDA+Autograd+%26+Tensor+Engine;Researching+Diffusion+Priors+for+Neural+Frame+Generation;Exploring+Reinforcement+Learning+in+Structured+Planning+(BlocksWorld);Understanding+how+machines+learn+structure%2C+not+just+patterns." alt="Typing SVG" />
  </a>
  <br/>
  <a href="https://www.linkedin.com/in/ishan-shishodiya-5100061b9/"><img src="https://img.shields.io/badge/LinkedIn-23272B?style=flat-square&logo=linkedin&logoColor=F7F6F2" alt="LinkedIn" /></a>
  &nbsp;
  <a href="mailto:sly.of.zero@gmail.com"><img src="https://img.shields.io/badge/Email-sly.of.zero%40gmail.com-23272B?style=flat-square&logo=gmail&logoColor=E07A5F" alt="Email" /></a>
</div>

---

### 🧭 Research Statement

I am an AI researcher with a background in systems engineering.

I care about how models work from the ground up. Most of my work involves building tensor engines and autograd from scratch in C++ and CUDA, training diffusion models for video frame interpolation, and experimenting with reinforcement learning on planning problems.

<p align="center">
  <img src="./assets/research-architecture.svg" alt="Research Architecture & Exploration Pillars" width="100%" />
</p>

---

### 🔬 Core Research Focus

* **Tensor Engines & Compute**: Building an autograd engine and tensor library from scratch in C++ and CUDA (`MyTorch`), focusing on computation graphs, custom kernels, and GPU memory layouts.
* **Diffusion & Frame Generation**: Working with diffusion models and flow matching for video frame interpolation, generating in-between frames from past and future context.
* **Reinforcement Learning & Planning**: Testing RL algorithms on structured environments like BlocksWorld with sparse rewards, studying state representation and credit assignment.

---

### 🛠️ Projects & Research Code

<table>
  <tr>
    <td width="50%" valign="top">
      <h4>⚡ <code>MyTorch</code>: C++ and CUDA Tensor Engine</h4>
      <p>A deep learning tensor library and autodiff engine built from scratch in C++ and CUDA to understand GPU execution and memory management directly.</p>
      <ul>
        <li>Dynamic computation graph with reverse-mode autodiff</li>
        <li>Custom CUDA kernels for matrix multiplication, activations, and reductions</li>
        <li>Strided N-dimensional tensors and custom memory allocation</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h4>🎞️ Video Frame Interpolation with Diffusion</h4>
      <p>Using diffusion models to generate intermediate video frames from surrounding frames, handling non-linear motion and occlusions.</p>
      <ul>
        <li>Conditioning diffusion models on past and future frames</li>
        <li>Temporal attention to maintain consistency across frames</li>
        <li>Comparing diffusion-based generation with optical flow methods</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>🧱 Reinforcement Learning for Planning (BlocksWorld)</h4>
      <p>Training RL agents to solve structured planning tasks like BlocksWorld where rewards are sparse and actions depend on object relationships.</p>
      <ul>
        <li>State representations for relational planning environments</li>
        <li>Hindsight Experience Replay (HER) to learn from failed attempts</li>
        <li>Comparing learned policies against classical search (A*)</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h4>📐 Paper Reproductions</h4>
      <p>Clean, minimal implementations of foundational papers to understand the details that matter during training.</p>
      <ul>
        <li>DDPM and DDIM with custom sampling schedules</li>
        <li>Flow Matching and optimal transport paths</li>
        <li>PPO on Gymnasium control environments</li>
      </ul>
    </td>
  </tr>
</table>

---

### 💻 Technical Tooling

<p align="left">
  <!-- Core ML / Frameworks -->
  <img src="https://img.shields.io/badge/PyTorch-23272B?style=flat-square&logo=pytorch&logoColor=EE4C2C" alt="PyTorch" />
  <img src="https://img.shields.io/badge/CUDA-23272B?style=flat-square&logo=nvidia&logoColor=76B900" alt="CUDA" />
  <img src="https://img.shields.io/badge/Gymnasium-23272B?style=flat-square&logo=openai&logoColor=white" alt="Gymnasium" />
  <img src="https://img.shields.io/badge/NumPy-23272B?style=flat-square&logo=numpy&logoColor=4DABCF" alt="NumPy" />
  <img src="https://img.shields.io/badge/Weights_%26_Biases-23272B?style=flat-square&logo=weightsandbiases&logoColor=FFBE00" alt="WandB" />
  <br/>
  <!-- Systems & Languages -->
  <img src="https://img.shields.io/badge/C%2B%2B-23272B?style=flat-square&logo=c%2B%2B&logoColor=00599C" alt="C++" />
  <img src="https://img.shields.io/badge/Python-23272B?style=flat-square&logo=python&logoColor=3776AB" alt="Python" />
  <img src="https://img.shields.io/badge/CMake-23272B?style=flat-square&logo=cmake&logoColor=064F8C" alt="CMake" />
  <img src="https://img.shields.io/badge/Linux-23272B?style=flat-square&logo=linux&logoColor=FCC624" alt="Linux" />
  <img src="https://img.shields.io/badge/Docker-23272B?style=flat-square&logo=docker&logoColor=2496ED" alt="Docker" />
</p>

---

### 📚 Research Tracker & Reading Log

<details>
  <summary><b>Current Literature Queue & Completed Deep Dives (Click to expand)</b></summary>
  <br/>

| Topic | Paper / Resource | Focus & Notes |
| :--- | :--- | :--- |
| **Diffusion Models** | *Denoising Diffusion Probabilistic Models (Ho et al.)* | Derivation of the variational bound and noise schedules |
| **Flow Matching** | *Flow Matching for Generative Modeling (Lipman et al.)* | Straight vector fields and optimal transport paths |
| **Video Generation** | *Diffusion Models for Video Generation & Interpolation* | Temporal cross-attention and conditioning on surrounding frames |
| **RL & Planning** | *Reinforcement Learning in Relational Domains* | State representations and credit assignment in BlocksWorld |
| **GPU Architecture** | *Programming Massively Parallel Processors (Kirk & Hwu)* | Memory coalescing, shared memory, and warp divergence |

</details>

---

### 📊 GitHub Activity

<p align="center">
  <img src="https://github-readme-stats-eight-theta.vercel.app/api?username=slyofzero&show_icons=true&border_color=363C42&bg_color=23272B&title_color=F7F6F2&icon_color=E07A5F&text_color=B5B0A6" alt="GitHub Stats" height="175" />
  &nbsp;
  <img src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=slyofzero&layout=compact&border_color=363C42&bg_color=23272B&title_color=F7F6F2&text_color=B5B0A6" alt="Top Languages" height="175" />
</p>

<p align="center">
  <img src="https://streak-stats.vercel.app/?user=slyofzero&border=363C42&background=23272B&ring=E07A5F&fire=E07A5F&currStreakLabel=E07A5F&currStreakNum=F7F6F2&sideNums=F7F6F2&sideLabels=B5B0A6&dates=9E998F" alt="GitHub Streak" width="62%" />
</p>

<p align="center">
  <img src="./assets/github-contributions.svg" alt="Contribution Graph" width="82%" />
</p>

---

<p align="center">
  <i>"Curious about how machines learn structure, not just patterns."</i>
</p>
