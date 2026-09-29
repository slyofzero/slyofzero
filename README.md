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

I am a systems engineer transitioning into AI research and applied AI science. My background is in production distributed systems, concurrency, and high-throughput pipelines.

In machine learning, I care about first-principles understanding over API wrapper engineering. Deep learning models are not black boxes to call; they are numerical systems shaped by hardware execution constraints, loss surface geometry, and optimization dynamics. My focus is on how representations emerge, how continuous generative flows evolve, and how to execute low-level tensor computations directly on hardware.

<p align="center">
  <img src="./assets/research-architecture.svg" alt="Research Architecture & Exploration Pillars" width="100%" />
</p>

---

### 🔬 Core Research Focus

* **Low-Level ML & Compute Engines**: Implementing automatic differentiation engines, custom CUDA kernels, memory allocators, and computation graphs from scratch in C++ and CUDA (`MyTorch`).
* **Generative Modeling & Continuous Dynamics**: Investigating Diffusion Models, Continuous Normalizing Flows, and Flow Matching. Using diffusion priors for neural video frame interpolation conditioned on bidirectional temporal context.
* **Reinforcement Learning & Structured Planning**: Evaluating policy and value function approximations in combinatorial environments with sparse reward landscapes (such as BlocksWorld), focusing on state abstractions and credit assignment.
* **Representation Learning & Latent Geometry**: Analyzing inductive biases, manifold regularization, and why learned representations generalize across relational structures instead of merely fitting training distributions.

---

### 🛠️ Projects & Research Code

<table>
  <tr>
    <td width="50%" valign="top">
      <h4>⚡ <code>MyTorch</code>: C++ and CUDA Tensor Engine</h4>
      <p>A from-scratch deep learning tensor library and reverse-mode automatic differentiation engine in C++ and CUDA, built to study hardware execution and memory mechanics without framework abstractions.</p>
      <ul>
        <li>Dynamic computation graph with reverse-mode automatic differentiation</li>
        <li>Custom CUDA kernels for GEMM, elementwise activations, and reductions</li>
        <li>Memory pooling and strided N-dimensional tensor layout implementations</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h4>🎞️ Neural Frame Interpolation with Diffusion Priors</h4>
      <p>Using score-based generative models to synthesize high-fidelity intermediate video frames, targeting temporal consistency and complex motion occlusions.</p>
      <ul>
        <li>Latent diffusion conditioned on preceding and succeeding frames</li>
        <li>Temporal cross-attention with perceptual and optical flow consistency penalties</li>
        <li>Benchmarking stochastic sampling trajectories against classical optical flow warping</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>🧱 Reinforcement Learning for Abstract Planning</h4>
      <p>Applying tabular and deep RL algorithms to structured symbolic planning benchmarks (such as BlocksWorld) under sparse reward signals.</p>
      <ul>
        <li>Value function approximation over relational and graph state representations</li>
        <li>Hindsight Experience Replay (HER) combined with curriculum exploration</li>
        <li>Measuring empirical sample complexity against heuristic symbolic search (A*, PDDL)</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h4>📐 Foundational Paper Reproductions</h4>
      <p>Minimal, clean implementations of foundational papers to inspect derivations, loss landscapes, and empirical optimization behavior.</p>
      <ul>
        <li>Denoising Diffusion Probabilistic Models (DDPM / DDIM) with custom noise schedules</li>
        <li>Flow Matching and Continuous Normalizing Flows (OT-CFM)</li>
        <li>PPO and Actor-Critic dynamics on discrete control benchmarks</li>
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

| Field | Paper / Topic | Core Focus / Notes |
| :--- | :--- | :--- |
| **Generative Models** | *Denoising Diffusion Probabilistic Models (Ho et al.)* | Derivation of the variational lower bound (ELBO) and noise schedule parametrization |
| **Flow Matching** | *Flow Matching for Generative Modeling (Lipman et al.)* | Optimal transport straight vector fields versus Brownian diffusion paths |
| **Frame Generation** | *Diffusion Models for Video Generation & Interpolation* | Bidirectional conditioning, temporal cross-attention, and latent consistency |
| **RL & Planning** | *Reinforcement Learning in Relational Domains* | Value iteration, graph state representations, and credit assignment in BlocksWorld |
| **Systems / Hardware** | *Programming Massively Parallel Processors (Kirk & Hwu)* | Warp divergence, memory coalescing, shared memory bank conflicts, and tiled execution |

</details>

---

### 📊 GitHub Activity

<p align="center">
  <img src="https://github-readme-stats-eight-theta.vercel.app/api?username=slyofzero&show_icons=true&border_color=363C42&bg_color=23272B&title_color=F7F6F2&icon_color=E07A5F&text_color=B5B0A6" alt="GitHub Stats" height="175" />
  &nbsp;
  <img src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=slyofzero&layout=compact&border_color=363C42&bg_color=23272B&title_color=F7F6F2&text_color=B5B0A6" alt="Top Languages" height="175" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=slyofzero&border=363C42&background=23272B&ring=E07A5F&fire=E07A5F&currStreakLabel=E07A5F&currStreakNum=F7F6F2&sideNums=F7F6F2&sideLabels=B5B0A6&dates=9E998F" alt="GitHub Streak" width="62%" />
</p>

<p align="center">
  <img src="./assets/github-contributions.svg" alt="Contribution Graph" width="82%" />
</p>

---

<p align="center">
  <i>"Curious about how machines learn structure, not just patterns."</i>
</p>
